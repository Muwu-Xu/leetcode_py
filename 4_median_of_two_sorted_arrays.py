class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
    ##brute force
            s = nums1 + nums2
        
            s.sort()
            
            n = len(s)
            
            if  n % 2 == 1: 
                return s[int(n/2)]
            else: 
                return (s[len(s)//2-1] + s[len(s)//2]) /2