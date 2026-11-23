class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set()

        for num in nums:
            numset.add(num)

        if len(nums) < 2:
            return 1

        numset = list(numset)
        numset.sort()
        print(numset)

        best = 1
        current = 1

        for i in range(len(numset)-1):
            if numset[i] + 1 == numset[i+1]:
                current += 1
                if current > best:
                    best = current
            else:
                current = 1
        return best
