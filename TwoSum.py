class Solution:
    def twoSum(self, nums, target: int):
        nums_set= set(nums)
        j= 0

        for i in range(0, len(nums)):
           
            remainder= target- nums[i]
            print(f'index{i}, number{nums[i]}, remainder{remainder}')
        
            if remainder in nums_set: #constant time
                j= nums.index(remainder)
                print(j)
                
                if j == i:
                    print(f'remaining list: {nums[i+1:]}')
                    if remainder in nums[i+1:]:
                        print('t')

                        j = nums[i+1:].index(remainder)
                        return[i, i+1+j]

            if nums[i] + nums[j] == target and i != j:
                return [i,j]





        

        