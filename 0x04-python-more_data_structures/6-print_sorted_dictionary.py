#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = sorted(
        list(a_dictionary)
    )  # (key=lambda x: x.lower()) if u want by ascii order
    for i in new_list:
        print("{:s}: {}".format(i, a_dictionary[i]))
