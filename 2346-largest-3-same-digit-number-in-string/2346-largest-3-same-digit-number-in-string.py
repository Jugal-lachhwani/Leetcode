class Solution:
    def largestGoodInteger(self, num: str) -> str:
        lgd = ""
        gd = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                gd = num[i] + num[i] + num[i]
                if lgd == "" or int(gd) > int(lgd): 
                    lgd = gd
                gd = ""

        return lgd