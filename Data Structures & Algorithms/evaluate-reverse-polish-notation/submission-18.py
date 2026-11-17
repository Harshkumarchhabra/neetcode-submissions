class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if len(stack)>=2:
                if i=='+':
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(a+b))
                elif i=='*':
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(a*b))
                elif i=='-':
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(b-a))
                elif i=='/':
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(b/a))
                else:
                    stack.append(int(i))
            else:
                stack.append(int(i))
        return stack[-1]