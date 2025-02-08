class Solution:
    def hasDuplicate(self, nums):
        check_here= set()
        for i in nums:
            if i in check_here:
                return True
            else:
                check_here.add(i)
        return False
 