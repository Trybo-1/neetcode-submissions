class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                hmap[nums[i]] = 1
        result = list(sorted(hmap.items(), key = lambda item: item[1], reverse = True))
        output = []
        for x in result:
            output.append(x[0])
        return output[:k]