class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_ascii= []
            t_ascii= []
            for i in range(0,26):
                s_ascii.append(0)
                t_ascii.append(0)
            
            for i in range(0, len(s)):
                

                position_s= ord(s[i])-97
                position_t= ord(t[i])-97


                s_ascii[position_s]= s_ascii[position_s]+ 1
                t_ascii[position_t]= t_ascii[position_t]+ 1
            
            return s_ascii == t_ascii
                
            
        else:
            return False 



        