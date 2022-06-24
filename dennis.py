from turtle import st


class Solution:
    
    def anaGram(self ,t : str, s : str) -> bool:
        if len(s) != len(s):
            return False

        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]]= 1  + countS.get(s[i],0)
            countT[t[i]]= 1  + countS.get(t[i],0)
        for j in countS:
            if countS[j] != countT[i]:
                return False
        return True


