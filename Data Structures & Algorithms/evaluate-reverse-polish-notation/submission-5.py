class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if  stack and  i=='+':
                stack.append(stack.pop()+stack.pop())
            elif  stack and  i=='-':
                a=stack.pop()
                b=stack.pop()
                stack.append((b-a))
            elif stack and  i=="*":
                stack.append(stack.pop()*stack.pop())
            elif  stack and  i=='/':
                a=stack.pop()
                b=stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(i))
        return stack[0]