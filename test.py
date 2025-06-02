def __in_repeat__():
    print("a")

def repeat(input):
    times = 0
    while times < input:
        times = times + 1
        print("time(s) = " + str(times))
        __in_repeat__()

def __main__():
    user_input = input("Time(s):")
    if user_input.isdigit():
        repeat(int(user_input))
    else:
        print("非法输入！")
        __main__()

__main__()