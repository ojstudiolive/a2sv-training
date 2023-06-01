class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word=""
        i = 0
        v = 0

        while i < len(word1) and v < len(word2):
            new_word += word1[i] + word2[v]
            i += 1
            v += 1

        if i < len(word1):
            new_word += word1[i:]
        if v < len(word2):
            new_word += word2[v:]
        return new_word
