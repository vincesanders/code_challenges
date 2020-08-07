def is_monotonic_array(a):
    is_descending = False
    is_ascending = False

    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            is_ascending = True
        elif a[i] > a[i + 1]:
            is_descending = True
        if is_ascending and is_descending:
            return False

    return True