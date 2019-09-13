#problem:https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=int((len(nums)-1)/2)
        right=len(nums)-1
        left=0
        while 0<=n<=len(nums)-1:
            if target>nums[-1]:
                return len(nums)
            elif target<nums[0]:
                return 0
            if target>nums[n] and target<nums[n+1]:
                return n+1
            elif target>nums[n-1] and target<nums[n]:
                return n
            elif target==nums[n]:
                return n
            if target<nums[n]:
                right=n-1
                n=int((right+left)/2)
            elif target > nums[n]:
                left=n+1
                n=int((left+right)/2)