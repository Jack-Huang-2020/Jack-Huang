def __in_repeat__():
    print("Debug")

def illegal_entry():
    print("Illegal entry!")
    print("")
    print("==================== Restart ====================")
    print("")

def repeat(def_input):
    times = 0
    debug_mode = input("Open Debug Mode?(Y/N):")
    if debug_mode not in "YNyn":
        illegal_entry()
        __main__()
    elif debug_mode in "Yy":
        while times < def_input:
            times = times + 1
            print("time(s) = " + str(times))
            __in_repeat__()
    else:
        while times < def_input:
            times = times + 1
            __in_repeat__()

def __main__():
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
