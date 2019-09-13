#problem:https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        modified='@#'+'#'.join(list(s))+'#$'   
		#we have to seperate string  with #, and plus different character¡Asince sometimes we have string like 'baab'
        P=[0]*len(modified)#[0,0,0......,0]
        max_P,longPalindromic=0,0
        C,R=1,1
        for i in range(1,len(modified)-2):
            mirr=C-(i-C)#locate mirror place for current center.
            if i<R:
                P[i]=min(R-i,P[mirr])#As I metion above, if it's in range P[i]>=P[mirror place]
            while modified[i+1+P[i]]==modified[i-1-P[i]]:#since P[i]>=P[mirror place] we only have to check the character out of P[i]
                P[i]+=1
            if i+P[i]>R:#If outside the range we should find our new center
                C=i
                R=C+P[C]
            if P[i]>=max_P:#record Longest Palindromic Substring
                max_P=P[i]
                longPalindromic=i
        ans=''.join(modified[longPalindromic-max_P:longPalindromic+max_P].split('#'))
        return ans