def productExceptSelf(nums):
    prefix_product_array= []
    suffix_product_array = []
    prefix_product= 1
    prefix_prev= 1
    suffix_product=1
    suffix_next=1


    for i in range(0, len(nums)):
        prefix_product_array.append(prefix_product*prefix_prev)
        prefix_prev= nums[i]
        prefix_product= prefix_product_array[-1]
            
    for i in range(len(nums)-1,-1, -1):
        suffix_product_array.append(suffix_product*suffix_next)
        suffix_next= nums[i]
        suffix_product= suffix_product_array[-1]

    suffix_product_array.reverse()

    output= []

    for i in range(0, len(nums)):
        output.append(prefix_product_array[i]*suffix_product_array[i])

    return output