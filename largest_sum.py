# given a list of numbers, return the largest sum
# [5,9,7,11] -> returns 20

def find_max_sum(nums):
    max_sum = 0

    for i in range(len(nums)):
        for j in range(len(nums)):
            if j <= i:
                continue
            cur_sum = nums[i] + nums[j]
            max_sum = max(cur_sum, max_sum)

    return max_sum

import time
time_1 = time.time()
max_sum = find_max_sum([5,9,7,8,1,10,4,234,494,574,384746])
time_2 = time.time()
print(time_2-time_1)

# O(n^2) - time complexity
# O(1) - space complexity

def find_max_sum(nums):
    large_first = max(nums[0], nums[1])
    if large_first == nums[0]:
        large_second = nums[1]
    else:
        large_second = nums[0]

    for i in range(2,len(nums)):
        if nums[i] > large_first:
            large_second = large_first
            large_first = nums[i]
        elif nums[i] > large_second:
            large_second = nums[i]

    return sum([large_first, large_second])

import time
time_1 = time.time()
max_sum = find_max_sum([5,9,7,8,1,10,4,234,494,574,384746])
time_2 = time.time()
print(time_2-time_1)

def find_max_sum_3(nums):
    nums = sorted(nums)
    return nums[-1] + nums[-2]

import time
time_1 = time.time()
max_sum = find_max_sum([5,9,7,8,1,10,4,234,494,574,384746])
time_2 = time.time()
print(time_2-time_1)