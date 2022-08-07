#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapS, mapT = {}, {}
        
        for str in range(len(s)):
            mapS[s[str]] = 1 + mapS.get(s[str], 0)
            mapT[t[str]] = 1 + mapT.get(t[str], 0)
        return True if mapS == mapT else False
