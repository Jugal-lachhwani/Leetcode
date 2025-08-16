class Solution(object):
    def maximum69Number (self, num):
        s = str(num)
        # for chr in range(len(s)):
        #     if s[chr] == '6':
        #         s[chr] = '9'
        #         break
        # return int(s)
        return int(s.replace('6','9',1))
        