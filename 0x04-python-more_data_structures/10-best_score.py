#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = 0
    max_key = None
    for k, v in a_dictionary.items():
        if v > max_value:
            max_value = v
            max_key = k
    return max_key


# THIS WORKS TOO
# def best_score(a_dictionary):
#     if a_dictionary is None:
#         return None
#     dic_values_list = list(a_dictionary.values())
#     max_value=max(dic_values_list)
#     max_index=dic_values_list.index(max_value)
#     keys_list = list(a_dictionary.keys())
#     best_key = keys_list[max_index]
#     return best_key
