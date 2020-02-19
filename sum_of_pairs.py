# [1, 2, 4, 6] 9 => False
# [1, 2, 4, 4] 8 => True

# negative numbers ok
# empty array => return none
# size limit of arrays

arr = [6, 4, 3, 2, 1, 7]
arr_sum = 9

def find_sum_pairs(arr, arr_sum):
    for i in arr:
        for j in arr:
            if i + j == arr_sum:
                return True
    return False

print(find_sum_pairs(arr, arr_sum))

# O(a * a) -> time complexity
# O(1) -> space complexity

def find_sum_pairs_2(arr, arr_sum):
    dict_2 = {}
    for i in range(len(arr)):
        if arr[i] in dict_2.keys():
            return True
        dict_2[arr_sum - arr[i]] = i
    return False

print(find_sum_pairs_2(arr, arr_sum))

# O(n) -> time complexity
# O(n) -> space complexity
