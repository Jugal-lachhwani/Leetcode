class Solution:
    def reverseWords(self, space: str) -> str:
        space = space.split(" ")
        s=[]
        for i in range(len(space)-1,-1,-1):
            if space[i] != "" and space[i] != " ":
                s.append(space[i])         
        return " ".join(s)