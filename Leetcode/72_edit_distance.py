# class Solution:
#     """This is to calculate transformation distance between word A to word B"""

#     def minDistance(self, word1: str, word2: str) -> int:
#         # going to follow Dynamic Programming array from bottom to top

#         dp_array = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

#         for i in range(len(word1) + 1):
#             dp_array[i][len(word2)] = len(word1) - i

#         for j in range(len(word2) + 1):
#             dp_array[len(word1)][j] = len(word2) - j

#         for i in range(len(word1) - 1, -1, -1):
#             for j in range(len(word2) - 1, -1, -1):
#                 if word1[i] == word2[j]:
#                     dp_array[i][j] = dp_array[i + 1][j + 1]

#                 else:
#                     dp_array[i][j] = 1 + min(
#                         dp_array[i][j + 1], dp_array[i + 1][j], dp_array[i + 1][j + 1]
#                     )

#         return dp_array[0][0]
#         # return dp_array


# s = Solution()
# print(s.minDistance(word1="horse", word2="ros"))  # output 3
# # print(s.minDistance(word1="intention", word2="execution"))  # output 5


def minDistance(word1: str, word2: str) -> int:
    # going to follow Dynamic Programming array from bottom to top

    dp_array = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    for i in range(len(word1) + 1):
        dp_array[i][len(word2)] = len(word1) - i

    for j in range(len(word2) + 1):
        dp_array[len(word1)][j] = len(word2) - j

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp_array[i][j] = dp_array[i + 1][j + 1]

            else:
                dp_array[i][j] = 1 + min(
                    dp_array[i][j + 1], dp_array[i + 1][j], dp_array[i + 1][j + 1]
                )

    return dp_array[0][0]
    # return dp_array

print(minDistance(word1="horse", word2="ros"))  # output 3
print(minDistance(word1="intention", word2="execution"))  # output 5