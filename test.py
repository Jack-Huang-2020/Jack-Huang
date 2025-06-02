def __in_repeat__():
    print("Debug")

def repeat(def_input):
    times = 0
    while times < def_input:
        times = times + 1
        print("time(s) = " + str(times))
        __in_repeat__()

def __main__():
    user_input = input("Time(s):")
    if user_input.isdigit():
        repeat(int(user_input))
    else:
        print("Illegal entry!")
        __main__()

if __name__ == __main__():
    __main__()