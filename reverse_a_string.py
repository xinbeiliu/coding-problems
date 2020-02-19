# https://leetcode.com/problems/reverse-string/submissions/

def reverse_str(s):
    # find first and last item in the list
    left_idx, right_idx = (0, len(s) -1)

    # do looping to move left and right index inwards
    while (left_idx < right_idx):
        # print(left_idx, right_idx)
        s[left_idx], s[right_idx] = s[right_idx], s[left_idx]
        left_idx += 1
        right_idx -=1
        # print(left_idx, right_idx)
        return s

print(reverse_str(["H","a","n","n","a","h"]))

# O(n) - time complexity
# O(1) - space complexity