import cv2
import numpy as np
import shutil

# ASCII字符集，按视觉效果从深到浅排列
ASCII_CHARS = '@%#*+=-:. '

def convert_to_ascii(gray_frame, cols=120, rows=40):
    # 调整图像尺寸以适配终端
    height, width = gray_frame.shape
    cell_width = width / cols
    cell_height = height / rows
    if cell_width == 0 or cell_height == 0:
        return ""

    ascii_frame = []
    for i in range(rows):
        y1 = int(i * cell_height)
        y2 = int((i + 1) * cell_height)
        if y2 >= height:
            y2 = height - 1

        line = []
        for j in range(cols):
            x1 = int(j * cell_width)
            x2 = int((j + 1) * cell_width)
            if x2 >= width:
                x2 = width - 1

            # 提取单元格并计算平均亮度
            cell = gray_frame[y1:y2, x1:x2]
            avg_brightness = np.mean(cell)

            # 将亮度转换为ASCII字符
            char_index = int(avg_brightness / 255 * (len(ASCII_CHARS)-1))
            line.append(ASCII_CHARS[char_index])
        ascii_frame.append(''.join(line))
    return '\n'.join(ascii_frame)

def main():
    # 获取终端尺寸
    terminal_cols, terminal_rows = shutil.get_terminal_size()
    display_cols = terminal_cols - 1
    display_rows = terminal_rows - 1  # 留一行显示提示信息

    # 初始化摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    try:
        print("正在捕捉画面，按 Q 退出...")
        while True:
            # 读取摄像头画面
            ret, frame = cap.read()
            if not ret:
                break

            # 转换为灰度图并水平翻转（镜像效果）
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.flip(gray, 1)

            # 转换为ASCII字符
            ascii_art = convert_to_ascii(gray, display_cols, display_rows)

            # 清屏并输出ASCII画面
            print(f"\033[0;0H{ascii_art}\n按 Q 退出", end='', flush=True)

            # 检测退出按键
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        print("\033[2J\033[H摄像头已关闭")  # 清屏

if __name__ == "__main__":
    main()