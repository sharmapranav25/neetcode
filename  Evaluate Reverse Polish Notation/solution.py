class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math_stack = []

        def perform_operation(stack, opertion):
            num2= stack.pop()
            num1= stack.pop()

            if opertion == '/':
                return int(num1/num2)
            if opertion == '*': 
                return (num1 * num2)
            if opertion == '+':   
                return (num1 + num2)
            if opertion == '-':
                return (num1 - num2)

        for i in tokens:
            if i == "+" or i == "*" or i == "-" or i == "/":
                print(math_stack)
                result = perform_operation(math_stack, i)
                math_stack.append(result)
                print(math_stack)

            else:
                math_stack.append(int(i))
                
        output = math_stack.pop()
        return output

        