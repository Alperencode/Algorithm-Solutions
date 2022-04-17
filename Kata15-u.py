# Count IP Addresses
# https://www.codewars.com/kata/526989a41034285187000de4/train/python
def ips_between(start, end):
    ip1, ip2 = [], []
    result = 0
    for i in start.split("."):
        ip1.append(int(i))
    for i in end.split("."):
        ip2.append(int(i))
    for i,v in enumerate(ip1):
        # I will continue from here
        pass

##Note: Didn't complete yet.