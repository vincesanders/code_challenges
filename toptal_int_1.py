def getChange(m, p):
    # return array [1c, 5c, 10c, 25c, 50c, $1]

    result = [0,0,0,0,0,0]

    if m <= 0:
        return result
    # round to nearest 100th
    target = int(m * 100 - p * 100)

    if target <= 0:
        return result

    while target > 0:
        if target >= 100:
            result[5] +=1
            target -= 100
        elif target >= 50:
            result[4] += 1
            target -= 50
        elif target >= 25:
            result[3] += 1
            target -= 25
        elif target >= 10:
            result[2] += 1
            target -= 10
        elif target >= 5:
            result[1] += 1
            target -= 5
        else:
            result[0] += 1
            target -= 1

    return result

# print(getChange(5, 0.99))

print(getChange(3.14, 1.99)) # should return [0,1,1,0,0,1]
print(getChange(3, 0.01)) # should return [4,0,2,1,1,2] *
print(getChange(4, 3.14)) # should return [1,0,1,1,1,0]
print(getChange(0.45, 0.34)) # should return [1,0,1,0,0,0]