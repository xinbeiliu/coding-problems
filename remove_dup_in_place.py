#bhttps://leetcode.com/problems/remove-duplicates-from-sorted-array/

def remove_dup(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

print(remove_dup([0,0,1,1,1,2,2,3,3,4]))

# O(n) - time complexity
# O(1) - space complexity
