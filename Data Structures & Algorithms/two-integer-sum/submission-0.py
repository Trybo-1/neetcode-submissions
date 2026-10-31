class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            num = target - nums[i]

            if num in hmap:
                return([min(i,hmap[num]),max(i,hmap[num])])
            
            hmap[nums[i]] = i
