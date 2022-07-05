class Solution(object):
    def capitalizeTitle(self, title):
        for i in title.split(" "):
            if len(i) <= 2:
                title = title.replace(i, i.lower())
                continue
            title = title.replace(i, i.capitalize())
        return title
            
# Testcases
# "capiTalIze tHe titLe"
# "First leTTeR of EACH Word"
# "i lOve leetcode"

# Status - Wrong Answer

# Cannot pass the this case
# Input: "Ewn R C HO O Omi cGl"
# Output: "Ewn r c ho o omi Cgl"
# Expected: "Ewn r c ho o Omi Cgl"

## In my solution, it need to capitalize the "O" in "Omi"
## Because len("omi") > 2, but it's not happening
## I'll try to figure out why but it need to work on the logic