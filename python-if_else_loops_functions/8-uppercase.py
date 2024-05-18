#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if ord[i] > 96 and ord[i] < 123:
            upper_char = chr(ord[i] - 32)
            result += "{}".format(upper_char)
        else:
            ans += "{}".format(i)
    print("{}".format(result))
