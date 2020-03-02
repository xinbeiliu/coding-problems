# https://leetcode.com/problems/two-sum/

def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return None

# O(n^2) - time complexity
# O(1) - space complexity

def two_sum_2(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        hash_map[nums[i]] = i

    for j in range(len(nums)):
        complement = target - nums[j]
        if complement in hash_map:
            if hash_map[complement] != j:
              return [j,hash_map[complement]]

# O(n) - time complexity
# O(n) - space complexity