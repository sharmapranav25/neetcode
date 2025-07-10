def longestConsecutive(nums):
    nums.sort()
    consecutive_seq_length = 0
    prev_num= 0
    max_lenght_found= 0
    for i in range(0,len(nums)):
        if i == 0:
            prev_num = nums[i]
            consecutive_seq_length +=1 
        elif nums[i] - 1 == prev_num:
            consecutive_seq_length +=1
            prev_num = nums [i]
        elif nums[i] - 1 != prev_num:
            max_lenght_found = consecutive_seq_length
            consecutive_seq_length = 0
            prev_num = nums[i]
            consecutive_seq_length +=1
        return max_lenght_found


