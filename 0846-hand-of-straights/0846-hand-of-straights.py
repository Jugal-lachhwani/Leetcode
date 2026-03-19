class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        import heapq
        
        while hand:
            heapq.heapify(hand)
            minNum = hand[0]
            for i in range(groupSize):
                # print(minNum + i)
                if (minNum+i) in hand:
                    hand.remove(minNum+i)
                else:
                    return False
            
        return True