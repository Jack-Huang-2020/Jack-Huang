import cv2
import numpy as np
import curses
from curses import wrapper
import time

# 全局配置参数
CHAR_SET = [' ', '░', '▒', '▓', '█']  # 灰度字符集
COLOR_MODE = False                     # 是否启用彩色模式
MAX_FPS = 30                           # 最大帧率限制
CHAR_ASPECT = 0.5                      # 字符宽高比修正系数

def get_terminal_size(stdscr):
    """安全获取终端尺寸"""
    rows, cols = stdscr.getmaxyx()
    return cols, rows  # 返回（宽度，高度）

def resize_frame(frame, target_size):
    """
    智能调整图像尺寸
    :param frame: 原始帧
    :param target_size: 目标尺寸 (width, height)
    :return: 调整后的图像
    """
    h, w = frame.shape[:2]
    t_width, t_height = target_size

    # 计算最佳缩放比例
    scale_w = t_width / w
    scale_h = (t_height * CHAR_ASPECT) / h
    scale = min(scale_w, scale_h)

    new_w = int(w * scale)
    new_h = int(h * scale / CHAR_ASPECT)

    # 边界检查
    new_w = min(new_w, t_width)
    new_h = min(new_h, t_height)

    # OpenCV尺寸调整
    resized = cv2.resize(frame, (new_w, new_h),
                        interpolation=cv2.INTER_AREA)

    # 创建画布并居中
    if COLOR_MODE:
        canvas = np.zeros((t_height, t_width, 3), dtype=np.uint8)
    else:
        canvas = np.zeros((t_height, t_width), dtype=np.uint8)

    y_start = (t_height - new_h) // 2
    x_start = (t_width - new_w) // 2

    # 处理不同模式下的数据赋值
    if COLOR_MODE:
        canvas[y_start:y_start+new_h, x_start:x_start+new_w, :] = resized
    else:
        gray_resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        canvas[y_start:y_start+new_h, x_start:x_start+new_w] = gray_resized

    return canvas

def convert_to_ascii(frame):
    """将帧转换为ASCII字符"""
    if COLOR_MODE:
        return convert_to_color(frame)

    # 直接使用灰度数据
    gray = frame if len(frame.shape) == 2 else cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    normalized = (255 - gray) / 255.0 if CHAR_SET[0] == ' ' else gray / 255.0
    indices = np.floor(normalized * (len(CHAR_SET)-1)).astype(int)

    return ["".join(CHAR_SET[i] for i in row) for row in indices]

def convert_to_color(frame):
    """转换为ANSI彩色字符串"""
    output = []
    for row in frame:
        line = []
        for pixel in row:
            b, g, r = pixel  # OpenCV使用BGR格式
            line.append(f"\033[48;2;{r};{g};{b}m ")
        output.append("".join(line))
    return output

def main(stdscr):
    # 初始化设置
    curses.curs_set(0)    # 隐藏光标
    stdscr.nodelay(1)     # 非阻塞输入
    stdscr.timeout(100)   # 刷新间隔

    # 初始化摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("无法访问摄像头")

    # 性能计数器
    last_time = time.time()

    try:
        prev_size = (0, 0)
        while True:
            # 动态获取终端尺寸
            term_size = get_terminal_size(stdscr)

            # 读取摄像头帧
            ret, frame = cap.read()
            if not ret:
                break

            # 尺寸变化时重新初始化
            if term_size != prev_size:
                prev_size = term_size
                stdscr.clear()

            # 调整帧尺寸
            processed = resize_frame(frame, term_size)

            # 转换输出格式
            output = convert_to_ascii(processed)

            # 渲染到终端
            stdscr.erase()
            try:
                for y, line in enumerate(output[:term_size[1]]):
                    stdscr.addstr(y, 0, line[:term_size[0]])
            except curses.error:
                pass
            stdscr.refresh()

            # 控制帧率
            delta = time.time() - last_time
            if delta < 1/MAX_FPS:
                time.sleep(1/MAX_FPS - delta)
            last_time = time.time()

            # 退出检测
            if stdscr.getch() == ord('q'):
                break

    except Exception as e:
        # 记录错误日志
        with open('camera_error.log', 'a') as f:
            f.write(f"{time.ctime()} - {str(e)}\n")
    finally:
        # 安全释放资源
        cap.release()
        try:
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()
        except:
            pass

if __name__ == "__main__":
    wrapper(main)