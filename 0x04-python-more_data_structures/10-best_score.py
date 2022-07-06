#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = 0
    for key in list(a_dictionary):
        if a_dictionary[key] > best:
            best = a_dictionary[key]
    if best != 0:
        return best
    return None
