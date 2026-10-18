class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        freqS = {}
        freqT = {}

        for char in s:
            if char in freqS:
                freqS[char] += 1
            else:
                freqS[char] = 1

        for char in t:
            if char in freqT:
                freqT[char] += 1
            else:
                freqT[char] = 1
        
        if freqS == freqT:
            return True

        else:
            return False