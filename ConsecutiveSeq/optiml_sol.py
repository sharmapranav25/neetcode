def longestConsecutive(nums):
    hash_map= {}
    seq_length= 0
    max_seq= 0

    def look_for_seq(key, seq_length, max_seq):
        seq_length +=1
        if hash_map.get(key) in hash_map.keys():
            return look_for_seq(hash_map.get(key))
        else:
            if max_seq < seq_length:
                max_seq= seq_length
                seq_length= 0
        return seq_length, max_seq

    for i in nums:
        if i in hash_map.keys:
            pass
        else:
            hash_map.update({i : i+1})
    
    for i in nums:
        if i-1 not in hash_map.keys(): ##start of sequence
            x= look_for_seq(i, seq_length, max_seq)
            seq_length=x[0]
            max_seq= x[1]
    return max_seq
    
