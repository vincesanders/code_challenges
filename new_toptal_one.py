def solution(t, r): # runtime: O(n), space: O(n)
    # find the number of groups
    # find the number of groups passed
    # create a dictionary
    tests = {} # space: O(n)
    passed = 0
    groups = 0
    for i in range(len(t)): # O(n)
        # if the last digit is a letter, it's part of a test group
        if t[i][-1].isdigit():
            # this is a test that is in its own group.
            # if their is only one test in the group, their is no need to add it to the tests dictionary
            # so add 1 to passed and groups
            if r[i] == 'OK':
                passed += 1
            groups += 1
        else:
            # the key will be the test name without the letter
            # the value will be an array of all the tests in a group.
            if t[i][:len(t[i]) - 1] in tests:
                # if the current test group is already in tests, 
                # add the value of the current test to it
                tests[t[i][:len(t[i]) - 1]].append(r[i])
            else:
                # ex: tests: { 'test1': ['OK', 'Runtime error] }
                tests[t[i][:len(t[i]) - 1]] = [r[i]]

    # iterate through all the items in the tests
    for _, array in tests.items(): # O(n) should have used .values
        groups += 1
        passed_all = True
        # ensure all items in test group were passed
        for score in array:
            if score is not 'OK':
                passed_all = False
        if passed_all:
            passed += 1

    # convert to percentage
    return passed * 100 // groups

'''
improvements:
    Check for edgecases:
        No input
        empty array
        passed = 0 # if passed is 0, it would cause 0 // 0, which would throw an error
'''

test = (['test1a', 'test2', 'test1b', 'test1c', 'test3'], ['Wrong answer', 'OK', 'Runtime error', 'OK', 'Time limit exceeded'])

print(solution(test[0], test[1]))