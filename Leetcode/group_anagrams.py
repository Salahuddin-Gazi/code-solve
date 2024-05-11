class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if anagram_map.get(sorted_word):
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]

        return [anagrams for anagrams in anagram_map.values()]


group_anagrams = Solution()
print(group_anagrams.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams.groupAnagrams(["eat", "tea"]))
print(group_anagrams.groupAnagrams(["eat", "ten"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
