class Solution:
    def hasDuplicate(self, nums):
        check_here= set() #space: O(n)
        try:
            for i in nums: #O(n)
                if i in check_here: #constant time
                    return True
                else:
                    check_here.add(i)
            return False
        except:
            print("An Error Occurred")
 