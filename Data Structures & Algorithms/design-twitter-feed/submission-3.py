import heapq
from collections import defaultdict, deque


class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.followee = defaultdict(dict)
        self.id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.id, tweetId))
        self.id += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = [p for p in self.posts[userId]]
        heapq.heapify(pq)
        while len(pq) > 10:
            heapq.heappop(pq)
        for k, v in self.followee[userId].items():
            if not v:
                continue
            for p in self.posts[k]:
                heapq.heappush(pq, p)
                while len(pq) > 10:
                    heapq.heappop(pq)
        ans = [0] * len(pq)
        i = len(ans)-1
        while pq:
            ans[i] = heapq.heappop(pq)[1]
            i -= 1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followee[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId][followeeId] = False
