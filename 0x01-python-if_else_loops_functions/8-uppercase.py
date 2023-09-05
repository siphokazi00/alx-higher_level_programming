#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            upper_char = char
        result += upper_char
    print("{}".format(result))


uppercase("Best School 98 Battery Street")
