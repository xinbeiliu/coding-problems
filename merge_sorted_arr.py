# https://leetcode.com/problems/merge-sorted-array/

def merge_sorted_arr_2(nums1, nums2):
    result = []
    size_1 = len(nums1)
    size_2 = len(nums2)
    i, j = 0, 0

    if size_1 == 0:
        return nums2
    if size_2 == 0:
        return nums1

    while i < size_1 and j < size_2:
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    while j < size_2:
        result.append(nums2[j])
        j += 1

    while i < size_1:
        result.append(nums1[i])
        i += 1

    return result

print(merge_sorted_arr_2([1,2,3,8], [4,5,6,7]))

# O(3(a+b)) - time complexity
# O(n) - space complexity
