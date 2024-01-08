#!/usr/bin/python3
def no_c(my_string):
    word = ""
    for i in range(len(my_string)):
        if my_string != "c" and my_string[i] != "C":
            word += my_string[i]
    return word
