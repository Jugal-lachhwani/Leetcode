class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l = [1 for i in text.split(" ")]
        words = text.split(" ")
        for b in brokenLetters:
            for i in range(len(words)):
                if b in words[i]:
                    l[i] = 0
        return sum(l)
