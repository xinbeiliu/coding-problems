# https://leetcode.com/problems/fizz-buzz/

def fizz_buzz(n):
    # do a for loop
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result

print(fizz_buzz(3))

# O(n) - time complextiy
# O(n) - space complexity