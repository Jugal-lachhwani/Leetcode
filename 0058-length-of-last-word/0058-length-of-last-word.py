class Solution:
    def lengthOfLastWord(self, s: str) -> int: 
        for i in range(len(s.split(" "))-1,-1,-1):
            if s.split(" ")[i] != "" and s.split(" ")[i] != " ":
                return len(s.split(" ")[i])