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

#question ask for Amazon, stream of numbers coming in and find the first pair of sum
# 3,9,1,7 should return [9,1] not [3,7]

# logic to solve, go though numbers, store complement in hashmap and if number in hashmap
# we found a pair, in hashmap, the value can be int but larger amount of int can cause overflow
# so that we can use boolean as value, we can only go over numbers once, when we
# go over the numbers, check if complement in hashmap, if not, add to hashmap then check
# number in number list