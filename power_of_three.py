# https://leetcode.com/problems/power-of-three/

def power_of_three(n):
    if n < 1:
        return False
    while (n % 3 == 0):
        n = n / 3
    return n == 1

print(power_of_three(27))

# O(log3n) - time complexity
# O(1) - space complexity