def solution(A):
    numbers = set()
    smallest_positive_integer = 1
    for i in range(len(A)):
        if A[i] <= 0:
            continue
        elif A[i] == smallest_positive_integer:
            new_spi_found = False
            while not new_spi_found:
                smallest_positive_integer += 1
                if smallest_positive_integer in numbers:
                    continue
                else:
                    new_spi_found = True

        numbers.add(A[i])
    
    return smallest_positive_integer