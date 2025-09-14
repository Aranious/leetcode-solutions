class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x= 0
        merged_list = []
        for i in range(m):
            merged_list.append(nums1[x])
            x +=1
        x= 0
        for i in range(n):
            merged_list.append(nums2[x])
            x +=1
        merged_list.sort()
        for i in range(m + n):
            nums1[i] = merged_list[i]