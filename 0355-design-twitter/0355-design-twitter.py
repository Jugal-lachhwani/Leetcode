class Twitter:

    def __init__(self):
        self.follows = {}
        self.posts = {}
        self.time = 1


    def postTweet(self, userId: int, tweetId: int) -> None:
        l = []
        if userId in self.posts:
            l = self.posts[userId]
        l.append((self.time,tweetId))
        self.time += 1
        self.posts[userId] = l

    def getNewsFeed(self, userId: int) -> List[int]:
        l_follows = list(self.follows.get(userId, []).copy())
        l_follows.append(userId)

        l_tweets = []
        for i in l_follows:
            for j in self.posts.get(i, []):
                time,id = j
                heapq.heappush(l_tweets, (-time,id))
        results = []
        for i in range(10):
            if l_tweets:
                time,id = heapq.heappop(l_tweets)
                results.append(id)
            
        return results 

    def follow(self, followerId: int, followeeId: int) -> None:
        l = set()
        if followerId in self.follows:
            l = self.follows[followerId]
        l.add(followeeId)
        self.follows[followerId] = l      

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            l = self.follows[followerId]
        else:
            return
        l.remove(followeeId)
        self.follows[followerId] = l


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)