# 2129. Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title/

class Solution(object):
    # long way:
    def capitalizeTitle(self, title):
        ans = []
        for item in title.split(" "):
            if len(item) <= 2:
                ans.append(item.lower())
            else:
                ans.append(item.lower().capitalize())
        return " ".join(ans)

    # short way:
    def capitalizeTitle(self, title):
        return " ".join(item.lower() if len(item)<=2 else item.lower().capitalize() for item in title.split(" "))

            
# Testcases
# "capiTalIze tHe titLe"
# "First leTTeR of EACH Word"
# "i lOve leetcode"

# Status - Success
# Runtime: 18 ms (Faster than 93.89% of Python submissions)
# Memory Usage: 13.4 MB