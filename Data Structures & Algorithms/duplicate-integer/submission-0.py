class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsNoDup = list(set(nums))
        nums.sort()
        numsNoDup.sort()

        if (nums==numsNoDup):
            return False
        else:
            return True




        