class Solution:
    def isValid(self, s: str) -> bool:
        curly_count = 0
        square_count = 0
        braces_count = 0
        lookfor_stack = []

        def brackets(s, i=0):
            nonlocal curly_count, square_count, braces_count

            if i == len(s):
                return not lookfor_stack  # Valid only if stack is empty

            brac = s[i]
            if brac == '(':
                curly_count += 1
                lookfor_stack.append(")")
                return brackets(s, i + 1)
            elif brac == '{':
                braces_count += 1
                lookfor_stack.append("}")
                return brackets(s, i + 1)
            elif brac == '[':
                square_count += 1
                lookfor_stack.append("]")
                return brackets(s, i + 1)
            elif brac in [')', '}', ']']:
                if not lookfor_stack or lookfor_stack[-1] != brac:
                    return False
                lookfor_stack.pop()
                if brac == ')':
                    curly_count -= 1
                elif brac == ']':
                    square_count -= 1
                elif brac == '}':
                    braces_count -= 1
                return brackets(s, i + 1)

            return True  # ignore non-bracket characters (optional)

        return brackets(s)
