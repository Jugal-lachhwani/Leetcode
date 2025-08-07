class Solution:
    def rotate(self, l: List[int], k: int) -> None:
        for i in range(k):
            l.insert(0,l[len(l)-1])
            l.pop(len(l)-1)

        