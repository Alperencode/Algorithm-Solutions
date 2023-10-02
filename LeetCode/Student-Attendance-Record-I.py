# 551. Student Attendance Record I - Easy
# https://leetcode.com/problems/student-attendance-record-i/

class Solution(object):
    def checkRecord(self, s):
        aCount = 0
        for i, v in enumerate(s):
            if v == "A":
                aCount += 1
            if v == "L":
                if s[i:i+3] == "LLL":
                    return False
        if aCount >= 2:
            return False
        return True

# Testcases
# "PPALLP"
# "PPALLL"
# "AA"

# Status - Accepted
