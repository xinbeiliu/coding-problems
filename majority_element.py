# https://leetcode.com/problems/majority-element/

def majority_element(nums):
    temp = {}
    majority_counter = len(nums) // 2

    for i in range(len(nums)):
        temp[nums[i]] = temp.get(nums[i], 0) + 1

    for k, v in temp.items():
        if v > majority_counter:
            return k


print(majority_element([3, 2, 3]))

# O(a + b) - time complexity
# O(n) - space complexity