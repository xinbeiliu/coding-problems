# https://leetcode.com/problems/contains-duplicate/

def contain_dup(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] == arr[j]:
                return True
    return False


print(contain_dup([1, 2, 3, 4]))


def contain_dup_2(arr):
    hash_map = {}
    for i in range(len(arr)):
        if arr[i] in hash_map:
            return True
        hash_map[arr[i]] = 1
    return False


print(contain_dup_2([1, 2, 3, 4]))

