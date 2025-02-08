class Solution:
    def topKFrequent(self, nums, k: int):
        freq_chart= {}
        top_k= []

        #making a freq_chart
        for i in nums:
            if i in freq_chart:
                freq_chart[i] = freq_chart[i] + 1
            else:
                freq_chart[i] = 1
        
        smallest_freq_k= freq_chart.get(nums[0])
        
        for i in freq_chart.keys():
            #filling top_k list
            if len(top_k) < k:

                #settitng the smallest_freq_k
                if  freq_chart.get(i) < smallest_freq_k:
                    smallest_freq_k = freq_chart.get(i)
                    
                top_k.append(i)
        
            else:

                freq_i= freq_chart.get(i) #freq of ith element

                #new element found with higher freq than one of the elements in top_k
                if freq_i > smallest_freq_k:
                    # print(i, freq_i, smallest_freq_k)
                    top_k.append(i)
                    
                    to_be_removed= int

                    smallest_freq_k= freq_chart.get(top_k[0])
                    #find the element that needs to removed 
                    for s in top_k:
                        if freq_chart.get(s) <= smallest_freq_k:
                            print(f'number: {s}, freq: {freq_chart.get(s)}')
                            smallest_freq_k = freq_chart.get(s)
                            to_be_removed= s
                        
                    print(top_k)    
                    top_k.remove(to_be_removed)
                    print(top_k)

        return top_k








            
    
            

        
        