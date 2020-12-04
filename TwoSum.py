#leetcode P1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            dct[nums[i]] = i
            
        
        for j in range(len(nums)):
            comp = target-nums[j]
            if comp in dct:
                if dct[comp]!=j:
                    return [j, dct[comp]]
