def solution(t, r):
    # find the number of groups
    # find the number of groups passed
    # create a dictionary
    tests = {}
    passed = 0
    groups = 0
    for i in range(len(t)):
        if t[i][-1].isdigit():
            # this is a test that is in its own group.
            if r[i] == 'OK':
                passed += 1
            groups += 1
        else:
            # the value will be an array of all the tests in a group.
            if t[i][:len(t[i]) - 1] in tests:
                tests[t[i][:len(t[i]) - 1]].append(r[i])
            else:
                tests[t[i][:len(t[i]) - 1]] = [r[i]]

    for _, array in tests.items():
        groups += 1
        passed_all = True
        for score in array:
            if score is not 'OK':
                passed_all = False
        if passed_all:
            passed += 1

    return passed * 100 // groups

test = (['test1a', 'test2', 'test1b', 'test1c', 'test3'], ['Wrong answer', 'OK', 'Runtime error', 'OK', 'Time limit exceeded'])

print(solution(test[0], test[1]))