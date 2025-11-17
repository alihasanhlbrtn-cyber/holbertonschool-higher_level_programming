#!/usr/bin/python3
import sys 
def add(a, b):
    result = a + b
    return result

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print(add(a, b))

