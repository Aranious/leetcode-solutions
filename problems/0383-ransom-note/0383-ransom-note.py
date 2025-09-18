class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_u_elements = {}
        ransomNote_u_elements = {}

        for i in magazine:
            if i in magazine_u_elements:
                magazine_u_elements[i] += 1  # increment existing count
            else:
                magazine_u_elements[i] = 1
        for i in ransomNote:       
            if i in ransomNote_u_elements:
                ransomNote_u_elements[i] += 1  # increment existing count
            else:
                ransomNote_u_elements[i] = 1 
        # 
        # 
        #     if i not in ransomNote_u_elements:
        #         ransomNote_u_elements.add(i)
                
        match = True
        for i in ransomNote_u_elements:
            if i in magazine_u_elements and ransomNote_u_elements[i] <= magazine_u_elements[i]:
                match = True
            else:
                match = False
                break
        return match