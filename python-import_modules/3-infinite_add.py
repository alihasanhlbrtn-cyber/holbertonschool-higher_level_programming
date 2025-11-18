#!/usr/bin/python3
#accepting inputs dynamically
import sys
if __name__ == "__main__":
    res = 0
    for arg in sys.argv[1:]:
        res += int(arg)
    print(res)
