import cv2
import numpy as np
import os
import curses

# 配置参数
CHAR_SET = [' ', '░', '▒', '▓', '█']  # 灰度字符集
CHAR_ASPECT = 0.5  # 终端字符宽高比修正
INVERT = True      # 适合深色终端

def get_terminal_size():
    """动态获取终端尺寸（列x行）"""
    try:
        from shutil import get_terminal_size
        cols, rows = get_terminal_size(fallback=(80, 24))
    except:
        cols, rows = 80, 24
    return cols, rows

def main(stdscr):
    # 初始化摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("摄像头不可用")

    # 初始化curses
    curses.curs_set(0)  # 隐藏光标
    stdscr.nodelay(1)   # 非阻塞输入

    try:
        while True:
            # 获取当前终端尺寸
            cols, rows = get_terminal_size()

            # 读取帧
            ret, frame = cap.read()
            if not ret:
                break

            # 转换为灰度图
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 计算目标尺寸（考虑字符宽高比）
            target_width = cols
            target_height = int(rows / CHAR_ASPECT)

            # 调整尺寸
            resized = cv2.resize(gray, (target_width, target_height),
                               interpolation=cv2.INTER_AREA)

            # 亮度处理
            if INVERT:
                resized = 255 - resized

            # 标准化到字符集范围
            normalized = resized / 255.0
            char_indices = np.floor(normalized * (len(CHAR_SET) - 1)).astype(int)

            # 构建输出字符串
            output = []
            for y in range(rows):
                if y < char_indices.shape[0]:
                    line = "".join([CHAR_SET[i] for i in char_indices[y]])
                    output.append(line)
                else:
                    output.append("")  # 填充空行

            # 清屏并输出
            stdscr.erase()
            for y, line in enumerate(output[:rows]):  # 确保不超过终端行数
                try:
                    stdscr.addstr(y, 0, line)
                except:
                    pass
            stdscr.refresh()

            # 退出检测
            if stdscr.getch() == ord('q'):
                break

    finally:
        cap.release()
        curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)