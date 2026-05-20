class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         return len(nums) != len(set(nums))


nums=[1,2,3,2,1,2,34,45,]
solution = Solution()
solution.hasDuplicate(nums)