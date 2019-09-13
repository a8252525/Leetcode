#problem:https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        com=''
        ans=[]
        def backtrack(com,next_digits):
            if len(next_digits)==0:
                ans.append(com)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(com+letter,next_digits[1:])
        if digits:
            backtrack('',digits)
        return ans
            