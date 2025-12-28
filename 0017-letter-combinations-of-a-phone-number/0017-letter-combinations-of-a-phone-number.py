class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        telephone = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        res = [""]

        for d in digits:
            new_res = []
            for prefix in res:
                for ch in telephone[d]:
                    new_res.append(prefix + ch)
            res = new_res

        return res        