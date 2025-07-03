class Solution:
    def groupAnagrams(self, strs):

        indices = {} #O(n) {space complexity}
        freq_chart= []
        final_group= []
        

        for i in range(25): #O(1) {time complexity}
            freq_chart.append(0)

        def ascii_coder(string):
            code= freq_chart.copy() #O(1) copy here will always be constant time because itsd always the same 26 elements. copy() itself stakes O(n) but n = 26

            for i in range(len(string)): #O(n) {time complexity}
                ascii= ord(string[i]) - ord('a')
                code[ascii] = code[ascii] +1 

            return code

        for i in strs: #O(n) {time complexity}
            indices[i] = ascii_coder(i)

        seen_indexes = set() #O(n) {space complexity}
        
        for i in range(0, len(strs)): # O(n){time complexity}

            if i in seen_indexes:
                print(f"Word has been seen. Word: {strs[i]}, seen_indexes: {seen_indexes}")
            else:
                sub_group= [strs[i]]
                print(f"Word has not been seen. Word: {strs[i]}, seen_indexes: {seen_indexes}")
                seen_indexes.add(i)

                for j in range(i+1 , len(strs)):#O(n^2) {Worst case time complexity}
                    print(strs[j], j)

                    if indices.get(strs[i]) == indices.get(strs[j]): #O(1)
                            print(f"anagram found: {strs[i]} and {strs[j]}, index: {i} and {j+i}")
                            seen_indexes.add(j)
                            sub_group.append(strs[j])
                            print(f'sub group: {sub_group}')

                final_group.append(sub_group)

        return final_group



        