# from typing import List


# class Solution:
#     """This is to find alien word order list"""

#     def alienOrder(self, words: List[str]) -> str:
#         adj = {c: set() for w in words for c in w}

#         for i in range(len(words) - 1):
#             w1, w2 = words[i], words[i + 1]

#             minLength = min(len(w1), len(w2))

#             if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
#                 return ""

#             for j in range(minLength):
#                 if w1[j] != w2[j]:
#                     adj[w1[j]].add(w2[j])
#                     break

#         visited = {}  # 0 -> visited, 1 -> visited in a cycle/loop
#         res = []

#         def dfs(c):
#             if c in visited:
#                 return visited[c] == 1

#             visited[c] = 1

#             for nb in adj[c]:
#                 if dfs(nb) == 1:
#                     return True

#             visited[c] = 0
#             res.append(c)

#         for c in adj:
#             if dfs(c):
#                 return ""

#         res.reverse()
#         return "".join(res)


# s = Solution()
# print(s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))  # result wertf
# print(s.alienOrder(["baa", "abcd", "abca", "cab", "cad"]))  # result "bdac"
# print(s.alienOrder(["caa", "aaa", "aab"]))  # result "cab"
# print(s.alienOrder(["z", "x", "z"]))  # result ""


def alienOrder(words) -> str:
    # This is to find alien word order list
    adj = {c: set() for w in words for c in w}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]

        minLength = min(len(w1), len(w2))

        if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
            return ""

        for j in range(minLength):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    visited = {}  # 0 -> visited, 1 -> visited in a cycle/loop
    res = []

    def dfs(c):
        if c in visited:
            return visited[c] == 1

        visited[c] = 1

        for nb in adj[c]:
            if dfs(nb) == 1:
                return True

        visited[c] = 0
        res.append(c)

    for c in adj:
        if dfs(c):
            return ""

    res.reverse()
    return "".join(res)

print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))  # result wertf
print(alienOrder(["baa", "abcd", "abca", "cab", "cad"]))  # result "bdac"
print(alienOrder(["caa", "aaa", "aab"]))  # result "cab"
print(alienOrder(["z", "x", "z"]))  # result ""