#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    arg_len = len(args) - 1
    print("{} {}{}".format(arg_len, "argument" if arg_len ==
          1 else "arguments", ":" if arg_len > 0 else "."))

    if arg_len > 0:
        for i in range(len(args)):
            if i != 0:
                print("{}: {}".format(i, args[i]))
