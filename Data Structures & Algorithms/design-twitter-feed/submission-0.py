from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.time = 0                          # 全局时间戳,越大越新
        self.tweets = defaultdict(list)        # userId -> [(time, tweetId), ...]
        self.following = defaultdict(set)      # userId -> 关注的人集合

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1                         # 每发一条,时间+1

    def getNewsFeed(self, userId):
        # 候选人 = 自己 + 关注的人
        people = self.following[userId] | {userId}

        # 把所有候选人的推文汇总
        candidates = []
        for person in people:
            candidates.extend(self.tweets[person])

        # 按时间从新到旧排序,取前 10 条的 tweetId
        candidates.sort(reverse=True)          # time 大的在前
        return [tid for _, tid in candidates[:10]]

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)  # discard 不存在也不报错