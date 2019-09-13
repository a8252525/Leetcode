#problem:https://leetcode.com/problems/string-to-integer-atoi/

import re
class Solution:
    def myAtoi(self, string: str) -> int:
        l=[]
        ans=''
        l=re.match(r"^([+-]?\d+\.?\d*).*$",string.strip())
        if not l:
            return 0
        ans=l.group(1)
        ans=float(ans)
        if ans>(2**31-1):
            return 2**31-1
        elif ans<-(2**31):
            return -(2**31)
        else:
            return int(ans)