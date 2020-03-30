# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed
# that each log has at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier, with the
# identifier used in case of ties.  The digit-logs should be put in their original order.
#
# Return the final order of the logs.

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

def reorder_log_files(logs):

    res1, res2 = [], []

    for log in logs:
        if log.split()[1].isdigit():
            res2.append(log)
        else:
            res1.append(log.split())

    res1.sort(key=lambda x:x[0])
    res1.sort(key=lambda x:x[1:])

    for i in range(len(res1)):
        res1[i] = " ".join(res1[i])

    res1.extend(res2)

    return res1

print(reorder_log_files(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

