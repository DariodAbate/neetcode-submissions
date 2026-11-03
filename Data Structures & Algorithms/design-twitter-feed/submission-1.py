import heapq

class Twitter:

    def __init__(self):
        # pull model: we only need who each user follows, not who follows them
        self.followeesByUser = {}
        # global counter to order tweets across different users
        self.ts = 0
        self.postsByUser = {}
        self.MAX_POSTS = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.postsByUser:
            self.postsByUser[userId] = deque()
        posts = self.postsByUser[userId]

        posts.append([self.ts, tweetId])
        if len(posts) > self.MAX_POSTS:
            posts.popleft()
        self.ts += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        followees = set()
        # copy the set so reading the feed doesn't change who the user follows
        if userId in self.followeesByUser:
            followees.update(self.followeesByUser[userId])

        followees.add(userId) # consider also himself

        heap = []
        for followee in followees:
            # never posted
            if followee not in self.postsByUser:
                continue
            for ts, tweetId in self.postsByUser[followee]:
                heapq.heappush(heap, [ts, tweetId])
                if len(heap) > self.MAX_POSTS:
                    heapq.heappop(heap)

        res = []
        while heap:
            ts, tweetId = heapq.heappop(heap)
            res.append(tweetId)
        res.reverse() # most recent
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followeesByUser:
            self.followeesByUser[followerId] = set()
        followees = self.followeesByUser[followerId]
        followees.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followeesByUser:
            return
        followees = self.followeesByUser[followerId]

        if followeeId not in followees:
            return 
        followees.remove(followeeId)
        
