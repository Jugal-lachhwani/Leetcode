class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        d = {}
        max_len = 0
        for word in words:
            d[word] = 1
            for i in range(len(word)):
                if len(word) <= 1:
                    break
                part_word = word[:i] + word[i+1:]
                # print(word,part_word)
                if part_word in d:
                    d[word] = max(d[part_word] + 1,d[word])
            max_len = max(d[word],max_len)
            # print(d)
        return max_len