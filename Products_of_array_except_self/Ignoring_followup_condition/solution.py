def productExceptSelf(nums):
        number_of_zeros= 0 
        product= 1
        output= []
        for i in nums:
            if i == 0:
                if number_of_zeros == 0:
                    number_of_zeros +=1

                elif number_of_zeros >=1:
                    number_of_zeros +=1
                    product = product*0
            else:
                product= int(product *i)

        
        for i in nums:
            if number_of_zeros == 0:
                output.append(int(product/i))
            elif number_of_zeros == 1:
                if i == 0:
                    output.append(product)
                else:
                    output.append(0)

            elif number_of_zeros > 1:
                output.append(0)
            

        return output
        
        