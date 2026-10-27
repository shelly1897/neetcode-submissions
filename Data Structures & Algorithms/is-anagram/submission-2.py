class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq ={}
        for char in t:
            if char in freq:
                freq[char] +=1
            else:
                freq[char] = 1

        for char in s:
            if char not in freq:
                return False
            if freq[char] !=0:
                freq[char] = freq.get(char) - 1
            else:
                return False
            

        return True

        