#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    dic_values_list = sorted(list(a_dictionary.values()), reverse=True)
    return dic_values_list[0]
