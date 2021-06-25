import test

test_cases = [
    ('name', 'equal', 'Balazs'),
    ('name', 'not_equal', 'Balazs'),
    ('city', 'equal', 'Debrecen'),
    ('city', 'not_equal', 'Debrecen'),
    ('date', 'greater_than', '1997-04-18'),
    ('something', 'equal', 'nope'),
    ('number', 'equal', 1997),
    ('bool', 'not_equal', False)
]

input_indexes = [0, 1]

reduced_test_cases = test.reduce_test_cases(test_cases, input_indexes)
print(reduced_test_cases)
print(f'Original number of test cases: {len(test_cases)}, Reduced number of test cases: {len(reduced_test_cases)}')