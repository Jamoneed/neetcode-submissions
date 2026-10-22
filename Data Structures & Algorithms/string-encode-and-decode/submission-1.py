class Solution:

    def encode(self, strs: List[str]) -> str:

        #strings = ["hello", "world", "cat"]

        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string))+"#"+string
            # encoded_string = 5#hello5#world3#cat
        
        return encoded_string


    def decode(self, s: str) -> List[str]:

        decode_string = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            decode_string.append(word)

            i = j+1+length

        return decode_string

