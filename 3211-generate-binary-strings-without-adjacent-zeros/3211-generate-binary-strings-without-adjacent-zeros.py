class Solution:
    def validStrings(self, n: int) -> List[str]:

        def generate_binary(start,i,res,n):
            if i == n:
                res.append(start)
                return
            if start == "" or start[-1] == "1":
                generate_binary(start + "1",i+1,res,n)
                generate_binary(start+"0",i+1,res,n)
            if start and start[-1] == "0":
                generate_binary(start+"1",i+1,res,n)
        res = []
        generate_binary('',0,res,n)
        return res      