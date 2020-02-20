# https://leetcode.com/problems/defanging-an-ip-address/

def defang_ip(address):

    result = []
    for char in address:
        if char == '.':
            char = '[' + char + ']'
        result.append(char)

    return ''.join(result)

print(defang_ip('1.1.1.1'))