class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if len(stack)>=2:
                if i=='+':
                    a=int(stack.pop())
                    b=int(stack.pop())
                    stack.append(a+b)
                elif i=='-':
                    a=int(stack.pop())
                    b=int(stack.pop())
                    stack.append(b-a)
                elif i=='*':
                    a=int(stack.pop())
                    b=int(stack.pop())
                    stack.append(a*b)
                elif i=='/':
                    a=int(stack.pop())
                    b=int(stack.pop())
                    stack.append(int(b/a))
                else:
                    stack.append(int(i))
            else:
                stack.append(int(i))
        return stack[0]