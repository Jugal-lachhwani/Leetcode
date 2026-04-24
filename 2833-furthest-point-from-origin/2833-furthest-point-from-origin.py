class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        d = {"L":0,"R":0,"_":0}

        for i in moves:
            d[i] += 1
        
        return abs(d["L"] - d["R"]) + d["_"]
