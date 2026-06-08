import time

RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"

message = "LTC, welcome to the lesson of debugging"

left_blocks = 4
right_blocks = 4
spaces = 2

middle_width = left_blocks + spaces + len(message) + right_blocks
scan_width = 5
scan_start = -scan_width


def clear():
    print("\033c\033[3J", end="")


def scanned(index):
    return scan_start <= index < scan_start + scan_width


while True:
    clear()

    # Top green strip
    print(GREEN, end="")
    for i in range(middle_width):
        print("/" if i % 4 == 0 else "■", end="")
    print(RESET)

    print()
    print()

    # Middle red strip
    print(RED, end="")

    # Left red blocks: index 0-3
    for i in range(4):
        print("█" if scanned(i) else "▪", end="")

    # Space: index 4
    print(" ", end="")

    # Text starts at index 5
    for i in range(len(message)):
        index = i + 5
        char = message[i]

        if scanned(index):
            print(char.upper(), end="")
        else:
            print(char, end="")

    # Space after text
    print(" ", end="")

    # Right red blocks
    right_start = 5 + len(message) + 1

    for i in range(right_start, right_start + 4):
        print("█" if scanned(i) else "▪", end="")

    print(RESET)

    print()
    print()

    # Bottom green strip
    print(GREEN, end="")
    for i in range(middle_width):
        print("/" if i % 4 == 0 else "■", end="")
    print(RESET)

    time.sleep(0.03)

    scan_start += 1

    if scan_start > middle_width:
        scan_start = -scan_width
        time.sleep(0.36)