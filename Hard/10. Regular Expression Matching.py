import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p='^'+p+'$'
        a=bool(re.search(p,s))
        return a