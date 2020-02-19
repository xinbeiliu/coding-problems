# https://leetcode.com/problems/intersection-of-two-arrays-ii/

def intersection_arr(nums1, nums2):
    result = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            nums2.remove(nums1[i])
            result.append(nums1[i])
    return result


print(intersection_arr([2, 2], [2]))
# should return [2,2]
print(intersection_arr([4, 9, 5], [9, 4, 9, 8, 4]))


# should return [4,9]

# O(n^2) - time complexity
# O(n) - space complexity

def intersection_arr_2(nums1, nums2):
    hash_map = {}
    result = []
    # make nums2 into a dictionary
    for i in range(len(nums2)):
        hash_map[nums2[i]] = hash_map.get(nums2[i], 0) + 1

    for j in range(len(nums1)):
        if nums1[j] in hash_map:
            result.append(nums1[j])
            del hash_map[nums1[j]]
    return result


print(intersection_arr_2([2, 2], [2]))
# should return [2,2]
print(intersection_arr_2([3, 9, 5], [9, 4, 9, 8, 4]))


# should return [4,9]

# O(a + b) - time complexity
# O(n) - space complexity

def intersection_arr_sorted(nums1, nums2):
    # use two pointers
    result = []
    nums1.sort()
    nums2.sort()

    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            # progress with nums2
            j += 1
        else:
            # progress with nums1
            i += 1

    return result


print(intersection_arr_sorted([2, 2], [2]))
# should return [2,2]
print(intersection_arr_sorted([4, 9, 5], [9, 4, 9, 8, 4]))