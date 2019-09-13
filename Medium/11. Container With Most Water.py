#problem:https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_value,l,r=0,0,len(height)-1
        while l<r:
            wied=min(height[l],height[r])
            max_value=max(max_value,wied*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_value