class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        words_arr = [s, t]
        anagram_map = {}

        for word in words_arr:
            sorted_word = ''.join(sorted(word))
            if anagram_map.get(sorted_word):
                return True
            else:
                anagram_map[sorted_word] = [word]

        return False


sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("anagram", "nagarao"))
