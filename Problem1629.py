# 1629. Slowest Key - Easy
# https://leetcode.com/problems/slowest-key/
class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        slowestTime = releaseTimes[0]
        slowestChar = [keysPressed[0]]
        for i,v in enumerate(releaseTimes):
            currentTime = v - releaseTimes[i-1]
            if currentTime > slowestTime:
                slowestTime = currentTime
                slowestChar = [keysPressed[i]]
            elif slowestTime == currentTime:
                slowestChar.append(keysPressed[i])
        return sorted(slowestChar)[-1]

# Testcases
# [9,29,49,50]
# "cbcd"
# [12,23,36,46,62]
# "spuda"

# Status - Accepted