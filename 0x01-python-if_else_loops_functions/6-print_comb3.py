#!/usr/bin/python3

for i in range(0, 10):
    for j in range(i, 10):
        if i != j:
            if j != 9:
                print("{}{}".format(i, j), end=", ")
            if i == 8:
                print("{}{}".format(i, j))
