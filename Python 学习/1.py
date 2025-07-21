from random import random


def __result__(result):
    if result == "=":
        print("平局")
    elif result == "👸🥇":
        print("👸🥇")
    elif result == "🤖🥇":
        print("🤖🥇")
    else:
        __debug_switch__("Invalid Input!")


def __main__():
    princess = int(input())
    # __debug_switch__("Robot Output")
    if princess == 1 and robot == 1:
        __result__("=")
    elif princess == 1 and robot == 2:
        __result__("🤖🥇")
    elif princess == 1 and robot == 3:
        __result__("👸🥇")
    elif princess == 2 and robot == 1:
        __result__("👸🥇")
    elif princess == 2 and robot == 2:
        __result__("=")
    elif princess == 2 and robot == 3:
        __result__("🤖🥇")
    elif princess == 3 and robot == 1:
        __result__("🤖🥇")
    elif princess == 3 and robot == 2:
        __result__("👸🥇")
    elif princess == 3 and robot == 3:
        __result__("=")

def __debug_switch__(switch):
    if switch == "Robot Output":
        print("[Info] Robot output:" + str(robot))
    elif switch == "Invalid Input!":
        print("[ERR] Invalid Input!")

import random
robot = random.randint(1, 3)
__main__()