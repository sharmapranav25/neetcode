class Solution:
    encoding_char= '='

    def encode(self, strs: List[str], encoding_char = encoding_char) -> str:
        s= ''
        
        for i in strs:
            if encoding_char in i:
                print('the encoding character exsists in the original string, change the charater or your encoding algorithm')
                break
            s= s + i + encoding_char
        
        return s
    
        


    def decode(self, s: str, encoding_char= encoding_char) -> List[str]:

        decoded_s=[]
        word= ''
        added_a_word= 0
        for i in s:
            if added_a_word == 1:
                added_a_word= 0
                word= ''
            print(word)
            if i == encoding_char:
                decoded_s.append(word)
                added_a_word= 1
            word= word+i

        return decoded_s

    
                


