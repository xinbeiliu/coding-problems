# https://leetcode.com/problems/missing-number/

def missing_num(nums):
    result = sorted(nums)

    for num in range(len(nums)+1):
        if num not in result:
            return num

# print(missing_num([9,6,4,2,3,5,7,0,1]))

# O(nlgn) - time complexity
# O(n) - space complexity

def missing_num_2(nums):

  hash_map = {}
  for i in range(len(nums)):
      hash_map[nums[i]] = hash_map.get(nums[i],0) + 1

  for num in range(len(nums) + 1):
      if num not in hash_map:
          return num

print(missing_num_2([9,6,4,2,3,5,7,0,1]))

# O(2n) - time complexity
# O(n) - space complexity