class Solution:
    def intToRoman(self, a: int) -> str:
        ans = ""
        div = 1
        dic = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        while a >= 1:
            mod = int(a % 10)
            if mod >= 1 and mod<=3:
                for i in range(mod):
                    ans = dic[div] + ans
            elif mod == 4:
                ans = dic[div] + dic[5*div] + ans
            elif mod == 5:
                ans = dic[div*5] + ans
            elif mod >= 6 and mod<=8:
                for i in range(mod-5):
                    ans =  dic[div] + ans
                ans = dic[5*div] + ans
            elif mod == 9:
                ans = dic[div] + dic[10*div] + ans
            div = div * 10
            a = a/10
        return ans
