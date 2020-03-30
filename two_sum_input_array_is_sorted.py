# Given an array of integers that is already sorted in ascending order, find two numbers
# such that they add up to a specific target number. The function twoSum should return
# indices of the two numbers such that they add up to the target, where index1 must be
# less than index2.

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

def two_sum(numbers, target):
    i, j = 0, len(numbers)-1
    while i < j:
        total = numbers[i] + numbers[j]
        if total > target:
            j -= 1
        elif total < target:
            i += 1
        else:
            return [i+1, j+1]

print(two_sum([2,7,11,15],9))