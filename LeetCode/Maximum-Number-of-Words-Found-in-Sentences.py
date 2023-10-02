# 2114. Maximum Number of Words Found in Sentences - Easy
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution(object):
    def mostWordsFound(self, sentences):
        counter = len(sentences[0].split(" "))
        for i in sentences:
            if len(i.split(" ")) >= counter:
                counter = len(i.split(" "))
        return counter

# Testcases
# ["alice and bob love leetcode","i think so too","this is great thanks very much"]
# ["please wait","continue to fight","continue to win"]

# Status - Accepted
