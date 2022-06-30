#!/usr/bin/python3
import re
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    pattern = re.compile("^\_\_[a-zA-Z0-9]{0,}\_\_$")
    
    for name in names:
        if not pattern.match(name):
            print(name)
