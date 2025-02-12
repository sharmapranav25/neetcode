class Solution:
    #test
    def isPalindrome(self, s: str) -> bool:
        valid_char= set() #o(1)

        for i in range (0, 10): #o(1)
            valid_char.add(ord(str(i)))
    
        for i in range(ord('A'), ord('z')+1): #o(1)
            valid_char.add(i)
        

        valid_str= '' #o(n)

        for i in s: #o(n)
            
            if ord(i) in valid_char:
                valid_str= valid_str + i

        valid_str= valid_str.lower() 
        rev = valid_str[::-1]
        print(valid_str)
        print(rev)
        if rev == valid_str:
            return True
        return False 
        