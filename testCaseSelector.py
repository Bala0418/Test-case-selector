from test import TestBase

testCases = [
    ('name', 'equal', 'Balazs'),
    ('name', 'not_equal', 'Balazs'),
    ('city', 'equal', 'Debrecen'),
    ('city', 'not_equal', 'Debrecen'),
    ('date', 'greater_than', '1997-04-18'),
    ('something', 'equal', 'nope'),
    ('number', 'equal', 1997),
    ('bool', 'not_equal', False)
]

inputIndexes = [0, 1]

test_set = TestBase.make_set(testCases)

reducedTestCases = TestBase.reduce_test_cases(testCases, inputIndexes)
print(reducedTestCases)