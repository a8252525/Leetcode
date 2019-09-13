#problem:https://leetcode.com/problems/3sum/
class Solution(object):
    def twoSum(self,target,nums,ans):
        i=0
        j=len(nums)-1
        if j<0:
            return
        while i<j:
            if target==nums[i]+nums[j]:
                ans.add((-target,nums[i],nums[j]))
                i+=1
                j-=1
            elif target<nums[i]+nums[j]:
                j-=1
            else:
                i+=1

        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        for i in range(len(nums)):
            target=-nums[i]
            self.twoSum(target,nums[i+1:],ans)
        return list(ans)