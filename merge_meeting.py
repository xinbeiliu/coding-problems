# a meeting is stored as tuple of int (start_time, end_time)
# these integers represent the number of 30-minute blocks past 9am
# (2,3) meeting from 10-10:30am
# (6,9) meeting from 12-1:30pm
# write a function merge_ranges() that takes a list of multiple meeting time
# ranges and return s a list of condensed ranges

# [(0,1), (3,5), (4,8), (10,12), (9,10)]
# would return [(0,1),(3,8),(9,12)]

# (3,5) vs (4,8) -> 5 is greater than 4 (end_time (1st) > start_time(2nd)
# (9,10) vs (10,12) -> 10 is equal 10 (end_time(1st) == start_time)2nd)
# (1,5) vs (2,3) -> 3 is smaller than 5 (end_time(1st) > end_time(2nd))
# after sorting, [(0,1), (3,5), (4,8), (9,10), (10,12)]

def merge_meeting(meetings):

    sorted_meetings = sorted(meetings)
    merged = []
    for meeting in sorted_meetings:
        if not merged:
            merged.append(meeting)
        else:
            cur = merged[-1]
            if meeting[0] <= cur[1]:
                merged[-1] = (cur[0], max(cur[1], meeting[1]))
            else:
                merged.append(meeting)
    return merged


print(merge_meeting([(1, 10), (2, 6), (3, 5), (7, 9)]))

# O(nlogn) time, O(n) space


