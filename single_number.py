# https://leetcode.com/problems/single-number/

def single_number(arr):
    # looping through, check if the number is in another list
    seen = []
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.append(arr[i])
        else:
            seen.remove(arr[i])
    return seen[0]


print(single_number([2, 2, 1]))


# O(n^2) - time complexity
# O(n) - space complexity

def single_number_2(arr):
    seen_2 = {}

    for i in range(len(arr)):
        seen_2[arr[i]] = seen_2.get(arr[i], 0) + 1

    for k, v in seen_2.items():
        if v == 1:
            return k


print(single_number_2([2, 2, 1]))

# O(n) - time complexity
# O(n) - space complexity