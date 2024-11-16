import collections
from typing import List


class Solution:
    """This is to transform start word to en word using one transformation at a time, count of the changes will be the output"""

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

        visited = set([beginWord])
        q = collections.deque([beginWord])
        res = 1

        # print(nei)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    for nb in nei[pattern]:
                        if nb not in visited:
                            visited.add(nb)
                            q.append(nb)

            res += 1

        return 0


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
