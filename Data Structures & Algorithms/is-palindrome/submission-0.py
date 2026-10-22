class Solution:
    def isPalindrome(self, s: str) -> bool:

        s= s.lower()
        filtered = ""

        for char in s:
            if char.isalnum():
                filtered += char
        
        i = 0
        j = (len(filtered)) -1

        while i < j:
            if filtered[i] != filtered[j]:
                return False
            
            i+=1
            j-=1
        return True
