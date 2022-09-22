"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""


import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        
        keep = 1
        for n in nums:
            result.append(keep)
            keep*=n
        
        keep = 1
        for i in reversed(range(len(nums))):
            result[i]*=keep
            keep*=nums[i]
            
        return result
            