from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.tweet_feed = defaultdict(deque)
        self.followers = defaultdict(set)
        self.time = 0
    def postTweet(self, userId, tweetId):
        self.tweet_feed[userId].append((self.time, tweetId))
        if len(self.tweet_feed[userId]) > 10:
            self.tweet_feed[userId].popleft()
            self.time -= 1
    def getNewsFeed(self, userId):
        followee = self.followers[userId]
        candidates = []
        for i in followee:
            candidates += self.tweet_feed[i]
        candidates += self.tweet_feed[userId]
        result = []
        while candidates and len(result) < 10:
            result.append(heapq.heappop(candidates)[1])
        return result








       

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
    def unfollow(self, followerId, followeeId):
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

       