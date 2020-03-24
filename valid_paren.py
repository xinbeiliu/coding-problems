# https://leetcode.com/problems/valid-parentheses/

def valid_paren(s):
    stack = []
    hash_map = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in hash_map.values():
            stack.append(char)
            print(stack)
        elif char in hash_map.keys():
            if stack == [] or hash_map[char] != stack.pop():
                return False

    return stack == []


print(valid_paren("{[]}"))  # True
# print(valid_paren("(]"))  # False
# print(valid_paren("()[]{}"))  # True
# print(valid_paren("([)]"))  # False
# print(valid_paren(""))  # True
# print(valid_paren("()"))  # True