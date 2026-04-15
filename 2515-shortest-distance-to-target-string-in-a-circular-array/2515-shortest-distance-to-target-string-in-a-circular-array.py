class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        doubleWords = words + words
        i = 0
        chance = 0
        sl = startIndex
        sr = startIndex
        while chance < len(words):
            if words[sl] == target:
                return chance
            if words[sr] == target:
                return chance
            chance += 1
            sl -= 1
            if sl == -1:
                s = len(words)-1
            sr = (sr + 1)%len(words)
        return -1
            


            