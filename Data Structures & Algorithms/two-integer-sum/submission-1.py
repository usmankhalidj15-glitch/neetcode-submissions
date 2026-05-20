class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

nums = [2,3,4,5,32,4,5]
target=7

solution = Solution()

print(solution.twoSum(nums,target))
