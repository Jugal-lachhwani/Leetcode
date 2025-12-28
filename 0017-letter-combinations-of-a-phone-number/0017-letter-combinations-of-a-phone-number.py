class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        telephone = {"2":"abc","3":"def","4":"ghi","5":"jhl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        l = []
        if len(digits) == 1:
            for d in telephone[digits[0]]:
                l.append(d)
        elif len(digits) == 2:
            for d1 in telephone[digits[0]]:
                for d2 in telephone[digits[1]]:
                    l.append(d1 + d2)
        elif len(digits) == 3:
            for d1 in telephone[digits[0]]:
                for d2 in telephone[digits[1]]:
                    for d3 in telephone[digits[2]]:
                        l.append(d1 + d2 + d3)
        elif len(digits) == 4:
            for d1 in telephone[digits[0]]:
                for d2 in telephone[digits[1]]:
                    for d3 in telephone[digits[2]]:
                        for d4 in telephone[digits[3]]:
                            l.append(d1 + d2 + d3+ d4)        
        return l