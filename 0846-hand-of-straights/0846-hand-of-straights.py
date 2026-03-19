class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        mp = Counter(hand)

        # iterating over keys in sorted order
        for key in sorted(mp.keys()):
            if mp[key] > 0:
                count = mp[key]
                # checking for consecutive cards in groupSize
                for i in range(groupSize - 1, -1, -1):
                    mp[key + i] -= count
                    if mp[key + i] < 0:
                        return False
        return True