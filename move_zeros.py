# https://leetcode.com/problems/move-zeroes/

def move_zeros(arr):
    # do it in place
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr

print(move_zeros([0, 1, 0, 3, 12]))

# O(n) - time complexity
# O(1) - space complexity