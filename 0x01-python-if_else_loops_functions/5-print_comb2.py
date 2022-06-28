#!/usr/bin/python3

for i in range(0, 100):
    if i < 99:
        print("{}".format(i if i > 9 else f"0{i}"), end=", ")
    else:
        print("{}".format(i))
