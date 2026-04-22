class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for queryWord in queries:
            for dicWord in dictionary:
                cnt = 0
                for i in range(len(queryWord)):
                    if queryWord[i] != dicWord[i]:
                        cnt += 1
                if cnt <= 2:
                    ans.append(queryWord)
                    break
        return ans