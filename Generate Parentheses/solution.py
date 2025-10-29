def generateParenthesis(n):
        result = []

        def backtrack(path, open_count, close_count, stack_level):
            print(f'stack level:{stack_level}')
            if len(path) == 2 * n:
                print(f"FORMED...stack level:{stack_level}, open_count: {open_count}, close_count: {close_count}'")
                result.append(path)
                return

            if open_count < n:
                print(f'OPEN...stack level:{stack_level}, open_count: {open_count+1}, close_count: {close_count}')
                backtrack(path + '(', open_count + 1, close_count, stack_level+1)
                print(f"open stack pop, stack level: {stack_level}")
                

            if close_count < open_count:
                print(f'CLOSE...stack level:{stack_level}, open_count: {open_count}, close_count: {close_count+1}')
                backtrack(path + ')', open_count, close_count +1 , stack_level +1)
                print(f"close stack pop, stack leve: {stack_level}")

        backtrack('', 0, 0, 0)
        return result