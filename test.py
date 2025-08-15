def __in_repeat__():
    print("Debug")
    # Debug Mode

def illegal_entry():
    # 非法输入
    print("Illegal entry!")
    print("")
    print("==================== Restart ====================")
    print("")

def repeat(def_input):
    # 用户输入
    times = 0
    debug_mode = input("Open Debug Mode?(Y/N):")
    # 是否开启
    if debug_mode not in "YNyn":
        # 检查是否为非法输入
        illegal_entry()
        __main__()
    elif debug_mode in "Yy":
        # 是
        while times < def_input:
            times = times + 1
            print("time(s) = " + str(times))
            __in_repeat__()
    else:
        # 否
        while times < def_input:
            times = times + 1
            __in_repeat__()

def __main__():
    # 主程序
    user_input = input("Time(s):")
    if user_input.isdigit():
        repeat(int(user_input))
    elif user_input == "exit" or user_input == "quit":
        exit()
    else:
        illegal_entry()
        __main__()

if __name__ == __main__():
    __main__()
    # 运行
