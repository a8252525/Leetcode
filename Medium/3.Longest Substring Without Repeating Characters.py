class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_forall=max_curr=start=0
        dic={}
        for i,char in enumerate(s):
            if char in dic and dic[char]>=start:
            #如果有重複字元，且它的位置比開始位置更後面
            #(這個也就代表，這個字元還在我們現在的子字串中)
                max_forall=max(max_forall,max_curr)
                max_curr=i-dic[char]
                start=dic[char]+1
            else:
                max_curr+=1
            dic[char]=i
        return max(max_forall,max_curr)