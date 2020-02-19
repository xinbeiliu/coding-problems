# Merge two sorted Arrays
# [0, 3, 4, 31]
# [4, 6, 30]
# becomes [0, 3, 4, 4, 6, 30, 31]

# naive way and allow to use built-in function
def Merge_sorted_lists(lst_1, lst_2):
    result = lst_1 + lst_2
    return sorted(result)


print(Merge_sorted_lists([0, 3, 4, 31], [4, 6, 30]))


# O(a + b) -> space complexity
# O n(logn) -> time complexity

def Merge_sorted_lists_2(lst_1, lst_2):
    result = []
    i, j = 0, 0

    # check input
    if lst_1 == []:
        return lst_2
    elif lst_2 == []:
        return lst_1

    while i < len(lst_1) and j < len(lst_2):
        if lst_1[i] < lst_2[j]:
            result.append(lst_1[i])
            i += 1
        else:
            result.append(lst_2[j])
            j += 1
    return result + lst_1[i:] + lst_2[j:]


print(Merge_sorted_lists_2([0, 3, 4, 31], [1, 4, 6, 30, 999]))

# O (a + b) -> time complexity
# O(3 * a) -> space complexity