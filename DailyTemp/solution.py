def dailyTemperatures(temperatures):
    stack = []
    result= []
    last_val= 0


    def stack_pop (stack, result, i):
        last_in= stack.pop() 
        days_waited= i - last_in[1]
        result[last_in[1]] = days_waited

        if len(stack)== 0 or stack[-1][0] >= temperatures[i]:
            return 

        elif stack[-1][0] < temperatures[i]:
            stack_pop(stack,result, i)


        

    for i in range(0, len(temperatures)):
        result.append(0)
        if len(stack) == 0:
            stack.append((temperatures[i], i))
            last_val= stack[-1]
        
        elif temperatures[i] <= last_val[0]:
            stack.append((temperatures[i], i))
            last_val= stack[-1]
        
        elif temperatures[i] > last_val[0]:
            stack_pop(stack, result, i)
            stack.append((temperatures[i], i))
            last_val= stack[-1]
            

    return result



        
        
        