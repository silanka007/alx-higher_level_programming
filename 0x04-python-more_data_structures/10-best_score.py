#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    keys = list(a_dictionary)
    if len(keys) == 0:
        return None

    best_key = keys[0]
    best = a_dictionary[best_key]

    for key in keys:
        if a_dictionary[key] > best:
            best = a_dictionary[key]
            best_key = key
    return best_key
