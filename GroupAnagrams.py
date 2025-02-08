class Solution:
    def groupAnagrams(self, strs):

        indices = {}
        freq_chart= []
        final_group= []
        

        for i in range(25):
            freq_chart.append(0)

        #print(freq_chart)

        def ascii_coder(string):
            code= freq_chart.copy()

            for i in range(len(string)):
                ascii= ord(string[i]) - ord('a')
                #print(ascii)
                #print(f'index_ascii: {index}')
                code[ascii] = code[ascii] +1

            return code

        for i in strs:
            indices[i] = ascii_coder(i)

        #print(indices)
        
        #print(f'indices: {indices}')

        seen_indexes = set()
        #works till here
        
        for i in range(0, len(strs)):
            

            if i in seen_indexes:
                print(f"Word has been seen. Word: {strs[i]}, seen_indexes: {seen_indexes}")
            else:
                sub_group= [strs[i]]
                print(f"Word has not been seen. Word: {strs[i]}, seen_indexes: {seen_indexes}")
                seen_indexes.add(i)

                for j in range(i+1 , len(strs)):
                    print(strs[j], j)

                    if len(strs[i]) == len(strs[j]):
                        print(f'possible anagram: {strs[j]}')

                        if indices.get(strs[i]) == indices.get(strs[j]):
                            print(f"anagram found: {strs[i]} and {strs[j]}, index: {i} and {j+i}")
                            seen_indexes.add(j)
                            sub_group.append(strs[j])
                            print(f'sub group: {sub_group}')

                final_group.append(sub_group)

        return final_group



        