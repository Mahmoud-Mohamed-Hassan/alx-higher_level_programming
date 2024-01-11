#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    if (type(roman_string) != str) or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if (
            i + 1 != len(roman_string)
            and roman_dic[roman_string[i]] < roman_dic[roman_string[i + 1]]
        ):
            ans = ans - roman_dic[roman_string[i]]
        else:
            ans = ans + roman_dic[roman_string[i]]
    return ans
