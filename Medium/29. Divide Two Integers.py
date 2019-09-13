#problem:https://leetcode.com/problems/divide-two-integers/submissions/
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        absDividend=abs(dividend)
        absDivisor=abs(divisor)
        ans=0
        while absDividend >= absDivisor:
            temp=0
            while absDividend >= absDivisor<<temp:
                absDividend-=absDivisor<<temp
                ans+=1<<temp
                temp+=1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            ans=-ans
        return ans if ans<2**31-1 else 2**31-1