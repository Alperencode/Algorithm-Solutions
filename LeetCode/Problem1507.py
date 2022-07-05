# 1507. Reformat Date - Easy
# https://leetcode.com/problems/reformat-date/
class Solution(object):
    def reformatDate(self, date):
        # YYYY-MM-DD
        months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept Sep","Oct","Nov","Dec"]
        info = date.split(" ")
        day = info[0][:-2]
        year = info[2]
        month = ""
        for m in months:
            if info[1] in m:
                month = months.index(m) + 1
                continue
        if len(str(month)) == 1:
            month = "0" + str(month)
        if len(str(day)) == 1:
            day = "0" + str(day)
            
        return f"{year}-{month}-{day}"

# Testcases
# "20th Oct 2052"
# "6th Jun 1933"
# "26th May 1960"

# Status - Accepted