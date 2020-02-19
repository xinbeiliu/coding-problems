# a large package can hold 5 items
# a small package can only hold 1 item
# the available number of both large and small packages are limited. all items must be placed in packages and used
# packages have to be filled up completely.
# write a function that calculates the minimum number of packages needed to hold given number of items. if it's not
# possible to meet the requirements, return -1
# 16 items, 2 large and 10 small packages, it should return 8 (2 large + 6 small)

def min_num_of_packages(items, available_large_packages, available_small_packages):
    hold_large = 5
    hold_small = 1

    for i in range(1,available_large_packages+1):
        if items - hold_large == 0:
            return i

        if items < hold_large:
            break

        items -= hold_large

    for j in range(1,available_small_packages+1):

        if items - hold_small == 0:
            return i + j

        items -= hold_small

    return -1

print(min_num_of_packages(16,4,10))