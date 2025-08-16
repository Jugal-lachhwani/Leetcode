class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            if n % 4 != 0:
                return False
            n = n / 4

        return True
        