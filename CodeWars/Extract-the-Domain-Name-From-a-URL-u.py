# Extract the domain name from a URL
# https://www.codewars.com/kata/514a024011ea4fb54200004b/

def domain_name(url):
    if url[0] == "h":
        if url[4] == "s":
            start = 8
        else:
            start = 7
    else:
        start = 4
    return url[start:].split(".")[0]

# Testcases
# "http://google.com" - "google"
# "http://google.co.jp" - "google"
# "www.xakep.ru" - "xakep"
# "https://youtube.com" - "youtube"

# Status: Passed: 25 Failed: 24
