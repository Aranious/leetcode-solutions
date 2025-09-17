class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        big_list = []
        for i in strs:
            letter_map = []
            for j in i: 
                letter_map.append(j)
            big_list.append(letter_map)

        common = []
        min_len = min(len(lst) for lst in big_list)
        for pos in range(min_len):
            char = big_list[0][pos]
            match = True
            for i in big_list:
                if i[pos] != char:
                    match = False
                    break
            if match:
                common.append(char)
            else:
                break

        return "".join(common)