import collections
from typing import List


class Solution:
    """This is to transform start word to en word using one transformation at a time, related to 127"""

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1 :]
                if pattern not in nei:
                    nei[pattern] = set()
                nei[pattern].add(w)

        ans = []
        queue = collections.deque([[beginWord]])
        visited = set()

        while queue:
            curlayer = set()

            for _ in range(len(queue)):
                curList = queue.popleft()
                lastWord = curList[-1]

                if lastWord == endWord:
                    ans.append(curList)
                
                # looking/searching next layer
                


s = Solution()
print(
    s.ladderLength(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"],
    )
)  # output 5
print(
    s.ladderLength(
        beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]
    )
)  # output 0
