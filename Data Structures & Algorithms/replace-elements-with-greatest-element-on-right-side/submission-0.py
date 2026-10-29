class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        best = -1

        for i in range(len(arr)):
            index = len(arr) - i -1

            temp = arr[index]

            arr[index] = best

            if temp > best:
                best = temp

        return arr

        