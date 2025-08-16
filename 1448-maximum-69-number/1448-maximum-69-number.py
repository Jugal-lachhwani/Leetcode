class Solution(object):
    def maximum69Number (self, num):
        s = str(num)
        return int(s.replace('6','9',1))
        