class Solution:
    def ladderLength(self, startWord: str, targetWord: str, wordList: List[str]) -> int:
    # Function to calculate the shortest transformation sequence length
        q = deque([(startWord, 1)])
        st = set(wordList)
        if startWord in st:
            st.remove(startWord)

        while q:
            word, steps = q.popleft()

            # If target word is found
            if word == targetWord:
                return steps

            # Try changing every character
            for i in range(len(word)):
                original = word[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in st:
                        st.remove(newWord)
                        q.append((newWord, steps + 1))
        return 0