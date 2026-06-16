class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        tList = list(t)

        sList.sort()
        tList.sort()

        if (tList == sList):
            return True
        else: 
            return False