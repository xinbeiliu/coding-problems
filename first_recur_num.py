# Given an array = [2,5,1,2,3,5,1,2,4]
# it should return 2
# Given an array = [2,1,1,2,3,5,1,2,4]
# it should return 1
# Given an array = [2,3,4,5]
# it should return None

# naive solution
def recurring_num(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    return None


print(recurring_num([2, 5, 5, 2, 3, 5, 1, 2, 4]))


# O(n^2) - time complexity
# O(1) - space complexity

# fast solution
def recurring_num_2(arr):
    result = {}
    for num in arr:
        if num in result:
            return num
        else:
            result[num] = True
    return None


print(recurring_num_2([2, 5, 5, 2, 3, 5, 1, 2, 4]))

# O(n) -> time complexity
# O(n) -> space complexity
