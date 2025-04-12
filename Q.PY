import cv2
import numpy as np
import shutil
import sys
from functools import lru_cache

# 增强的ASCII字符集（按亮度排序）
ASCII_CHARS = [' ', '·', '▪', '░', '▒', '▓', '▚', '▛', '▜', '▝', '▞', '█']
CHAR_ASPECT_RATIO = 0.45  # 字符宽高比调整参数

def get_terminal_size():
    return shutil.get_terminal_size(fallback=(120, 40))[::-1]  # (rows, cols)

@lru_cache(maxsize=256**3)
def ansi_color_code(r, g, b):
    # 优化颜色量化算法（6x6x6立方体 + 灰度扩展）
    if (r == g) and (g == b):
        return 232 + int(r / 10.6)  # 24级灰度
    return 16 + 36*(r//51) + 6*(g//51) + (b//51)

def capture_fullscreen():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    try:
        while True:
            # 获取动态终端尺寸
            term_rows, term_cols = get_terminal_size()

            # 读取摄像头帧
            ret, frame = cap.read()
            if not ret: break

            # 计算目标尺寸（考虑字符宽高比）
            char_height = 2  # 每个字符占用的垂直空间
            target_width = term_cols
            target_height = int(term_rows * char_height * CHAR_ASPECT_RATIO)

            # 自适应裁剪
            h, w = frame.shape[:2]
            aspect = w / h
            new_aspect = target_width / target_height

            # 根据宽高比进行智能裁剪
            if aspect > new_aspect:
                new_h = h
                new_w = int(h * new_aspect)
                frame = frame[:, (w-new_w)//2 : (w+new_w)//2]
            else:
                new_w = w
                new_h = int(w / new_aspect)
                frame = frame[(h-new_h)//2 : (h+new_h)//2, :]

            # 缩放并处理图像
            resized = cv2.resize(frame, (target_width, target_height))
            resized = cv2.GaussianBlur(resized, (3,3), 0)  # 降噪

        # 构建输出缓冲
        output = []
        for row in resized:
            line = []
            for bgr in row:
                r, g, b = bgr[2], bgr[1], bgr[0]
                # 修正后的亮度计算
                v = max(b, g, r)
                char_index = min(int(v/255 * (len(ASCII_CHARS)-1)), len(ASCII_CHARS)-1)
                char = ASCII_CHARS[char_index]
                line.append(f"\033[38;5;{ansi_color_code(r,g,b)}m{char}")
            output.append("".join(line))

            # 高效终端渲染
            sys.stdout.write(f"\033[0;0H{chr(27)}[?25l")  # 隐藏光标
            sys.stdout.write("\n".join(output))
            sys.stdout.flush()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        sys.stdout.write("\033[?25h")  # 恢复光标
        print("\n程序已终止")

if __name__ == "__main__":
    print("启动中... (按Q退出)")
    capture_fullscreen()