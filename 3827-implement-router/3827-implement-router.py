from collections import deque
from bisect import bisect_left, bisect_right

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.q = deque()  # FIFO queue for packets
        self.dupKey = set()  # detect duplicates
        self.desToTime = {}  # destination -> list of timestamps

    def makeKey(self, s: int, d: int, t: int) -> int:
        # encode packet as single integer to avoid strings
        return s * 10**10 + d * 10**5 + t

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = self.makeKey(source, destination, timestamp)
        if key in self.dupKey:
            return False

        # Evict oldest if memory full
        if len(self.q) == self.memoryLimit:
            old = self.q.popleft()
            oldKey = self.makeKey(old[0], old[1], old[2])
            self.dupKey.remove(oldKey)

            lst = self.desToTime[old[1]]
            lst.pop(0)  # remove oldest timestamp
            if not lst:
                del self.desToTime[old[1]]

        self.q.append((source, destination, timestamp))
        self.dupKey.add(key)
        if destination not in self.desToTime:
            self.desToTime[destination] = []
        self.desToTime[destination].append(timestamp)
        return True

    def forwardPacket(self):
        if not self.q:
            return []
        p = self.q.popleft()
        key = self.makeKey(p[0], p[1], p[2])
        self.dupKey.remove(key)

        lst = self.desToTime[p[1]]
        lst.pop(0)
        if not lst:
            del self.desToTime[p[1]]

        return [p[0], p[1], p[2]]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.desToTime:
            return 0
        lst = self.desToTime[destination]
        left = bisect_left(lst, startTime)
        right = bisect_right(lst, endTime)
        return right - left