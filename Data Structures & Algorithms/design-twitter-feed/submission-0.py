class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)    # userId -> [(time, tweetId)]
        self.following = defaultdict(set)  # userId -> set of followeeIds
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}
        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1          # newest tweet
                t, tid = self.tweets[u][idx]
                heapq.heappush(heap, (-t, tid, u, idx))
        feed = []
        while heap and len(feed) < 10:
            _, tid, u, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx > 0:                                # push that user's next older tweet
                t, ntid = self.tweets[u][idx - 1]
                heapq.heappush(heap, (-t, ntid, u, idx - 1))
        return feed
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)