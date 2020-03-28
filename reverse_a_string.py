# https://leetcode.com/problems/reverse-string/

def reverse_str(s):

    left_idx, right_idx = (0, len(s) -1)

    while (left_idx < right_idx):
        s[left_idx], s[right_idx] = s[right_idx], s[left_idx]
        left_idx += 1
        right_idx -=1


# O(n) - time complexity
# O(1) - space complexity

print(reverse_str(["h","e","l","l","o"]))