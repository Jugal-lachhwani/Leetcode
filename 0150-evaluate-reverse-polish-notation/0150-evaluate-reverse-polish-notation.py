class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        for i in tokens:
            if i not in ["+","-","/","*"]:
                l.append(i)
            else:
                int1 = int(l.pop(-1))
                int2 = int(l.pop(-1))
                if i == "+":
                    l.append(int1 + int2)
                elif i == "-":
                    l.append(int2 - int1)
                elif i == "/":
                    l.append(int2 / int1)
                else:
                    l.append(int1 * int2)
        return int(l.pop(-1))       