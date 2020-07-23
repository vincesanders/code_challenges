with open('./fraudulent_activity_notifications_test_case_1.txt') as test_case:
    for line in test_case:
        test_case_arr = line.split(' ')
    for i in range(len(test_case_arr)):
        test_case_arr[i] = int(test_case_arr[i])

# the key to this challenge was realizing you needed to use count sort.
# count sort is O(n) and is a great choice when we know we'll be sorting a finite number of numbers
def activityNotifications(expenditure, d):
    count_sort_list = [0] * 201

    for i in range(d):
        count_sort_list[expenditure[i]] += 1
    
    current = 0
    notifications = 0

    if d % 2 == 0:
        median_index = d // 2
    else:
        median_index = d // 2 + 1

    end = d

    while end < len(expenditure):
        median = get_median(count_sort_list, d, median_index)
        if expenditure[end] >= median * 2:
            notifications += 1

        count_sort_list[expenditure[current]] -= 1
        count_sort_list[expenditure[end]] += 1
        current += 1
        end += 1

    return notifications

def get_median(list, d, index):
    counter = 0
    left = 0

    while counter < index:
        counter += list[left] # increment counter by number of numbers at this index
        left += 1

    right = left
    left -= 1

    if counter > index or d % 2 != 0:
        return left
    else:
        #find the next number in the count_sort_list
        while list[right] == 0:
            right += 1
        return (left + right) / 2

a = [2,3,4,2,3,6,8,4,5]

print(activityNotifications(test_case_arr, 10000))

