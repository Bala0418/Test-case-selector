import random
from typing import Optional

class TestBase:
    def rand(x: int):
        return random.randrange(x)

    def make_set(testCases: list, indexes: Optional[list] = []):
        list = []
        final_list = []
        unique_test_cases = []
        if len(indexes) == 0:
            for number_of_attributes in range(len(testCases[0])):
                indexes.append(number_of_attributes)
        if indexes is not None:
            for i in indexes:
                for l in testCases:
                    list.append(l[i])
                for unique in list:
                    if unique not in unique_test_cases:
                        unique_test_cases.append(unique)
                final_list.append(unique_test_cases.copy())
                unique_test_cases.clear()
                list.clear()
        return final_list

    def reduce_test_cases(original_test_data: tuple, indexes: Optional[list] = []):
        final = []
        temp = []
        new_set = TestBase.make_set(original_test_data, indexes)
        for y in range(len(new_set[0])):
            for list in original_test_data:
                if new_set[0][y] == list[0]:
                    temp.append(list)
            if len(temp) > 1:
                temp.pop(TestBase.rand(len(temp)))
            final.extend(temp)
            temp.clear()
        return final