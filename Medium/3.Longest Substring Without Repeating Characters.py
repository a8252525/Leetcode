class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_forall=max_curr=start=0
        dic={}
        for i,char in enumerate(s):
            if char in dic and dic[char]>=start:
            #�p�G�����Ʀr���A�B������m��}�l��m��᭱
            #(�o�Ӥ]�N�N��A�o�Ӧr���٦b�ڭ̲{�b���l�r�ꤤ)
                max_forall=max(max_forall,max_curr)
                max_curr=i-dic[char]
                start=dic[char]+1
            else:
                max_curr+=1
            dic[char]=i
        return max(max_forall,max_curr)