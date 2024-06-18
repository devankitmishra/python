class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = 0
        for num in nums:
            totalSum |= num
        return totalSum << (n-1)