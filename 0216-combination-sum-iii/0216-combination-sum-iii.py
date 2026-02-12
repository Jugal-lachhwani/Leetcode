class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans=list()
        self.combine(k, n, [], 1, 0)
        return self.ans

    def combine(self, k: int, n: int, added: List[int], index: int, curr: int) -> None:
        if len(added)==k and curr==n:
            self.ans.append(added.copy())
            return
        if len(added)==k or curr>n or index>9:
            return
        added.append(index)
        self.combine(k, n, added, index+1, curr+index)
        added.pop()
        self.combine(k, n, added, index+1, curr)
        return