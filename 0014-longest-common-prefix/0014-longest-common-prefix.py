class Solution:
    def longestCommonPrefix(self, a: List[str]) -> str:
        c = ""
        s = a[0]
        for i in range(1,len(a)):
            c = ""
            k = 0
            while k<len(s) and k < len(a[i]):
                if s[k] == a[i][k] :
                    c += s[k]
                    k+=1
                else:
                    s = c
                    break
            s = c
        return s