import random
from typing import Optional, List, Tuple

def rand(x: int):
    return random.randrange(x)

def max_index(select_from: list):
    rows = []
    for i in select_from:
        rows.append(len(i))
    index =  rows.index(max(rows))
    return index

def make_set(test_cases: List[Tuple], indexes: Optional[List] = None):
    result = []
    for index in indexes:
        result.append(list(set([test_case[index] for test_case in test_cases])))
    return result

def reduce_test_cases(original_test_data: List[Tuple], indexes: Optional[List] = None):
    if not indexes:
        indexes = range(len(original_test_data[0]))
    new_set = make_set(original_test_data, indexes)
    index = max_index(new_set)
    final = []
    temp = []
    
    for x in range(len(new_set[index])):
        for rows in original_test_data:
            if rows.__contains__(new_set[index][x]):
                temp.append(rows)
        if len(temp) > 1:
            temp.pop(rand(len(temp)))
        final.extend(temp)
        temp.clear()
    return final