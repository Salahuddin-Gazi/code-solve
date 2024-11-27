from typing import List


class Solution:
    """This is to find the group anagram lists from the string lists"""

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            sorted_str = "".join(sorted(word))

            if anagram_map.get(sorted_str):
                anagram_map[sorted_str].append(word)
            else:
                anagram_map[sorted_str] = [word]

        return [word for word in anagram_map.values()]


group_anagrams = Solution()
print(group_anagrams.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams.groupAnagrams(["eat", "tea"]))
print(group_anagrams.groupAnagrams(["eat", "ten"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
