#problem:https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=map(str,list(str(int(''.join(list(map(str,digits))))+1)))

        return ans