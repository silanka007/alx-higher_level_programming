#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    keys = list(a_dictionary)
    if len(keys) == 0:
        return None

    best = a_dictionary[keys[0]]
    for key in keys:
        if a_dictionary[key] > best:
            best = a_dictionary[key]
    return best
