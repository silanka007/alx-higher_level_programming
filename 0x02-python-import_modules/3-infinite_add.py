#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    result = 0

    for i in range(len(args)):
        if i != 0:
            result += int(args[i])
    print(result)
