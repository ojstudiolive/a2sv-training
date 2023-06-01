class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        i = 0
        for c in s:
            if c == letter:
                i += 1
        return int((i/len(s))*100)
