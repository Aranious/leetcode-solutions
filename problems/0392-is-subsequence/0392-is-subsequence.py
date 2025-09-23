class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # using a hash map relizing the abs order in which they appear
        # seeing if the second str has the abc then to see if it has the order
        i, j = 0, 0 
        while i<len(s) and j <len(t):
            if s[i] == t[j]:
                i +=1
            
            j += 1
        return i == len(s)