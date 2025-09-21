class Router(object):

    def __init__(self, memoryLimit):
        self.memorylimit = memoryLimit
        self.l = deque()
        self.s = set()
        self.dest_map = defaultdict(SortedList)

    def addPacket(self, source, destination, timestamp):
        key = (source,destination,timestamp)
        if key in self.s:
            return False
        self.l.append(key)
        self.s.add(key)
        self.dest_map[destination].add(timestamp)

        if len(self.l) > self.memorylimit:
            s,d,t = self.l.popleft()                
            self.s.discard((s,d,t))
            self.dest_map[d].remove(t)
        return True

    def forwardPacket(self):
        if self.l:
            key = self.l.popleft()
            self.s.discard(key)
            self.dest_map[key[1]].remove(key[2])
            return key
        return []

        

    def getCount(self, destination, startTime, endTime):
        timestamps = self.dest_map[destination]
        return timestamps.bisect_right(endTime) - timestamps.bisect_left(startTime)
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)