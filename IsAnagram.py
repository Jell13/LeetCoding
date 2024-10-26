# -- IS ANAGRAM --
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkS = defaultdict()
        checkT = defaultdict()

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            checkS[s[i]] = checkS.get(s[i], 0) + 1
            checkT[t[i]] = checkT.get(t[i], 0) + 1

        return checkS == checkT
    