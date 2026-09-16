class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
                if i=='+':
                    f=stack.pop()
                    s=stack.pop()
                    stack.append(int(f+s))
                elif i=='-':
                    f=stack.pop()
                    s=stack.pop()
                    stack.append(int(s-f))
                elif i=='*':
                    f=stack.pop()
                    s=stack.pop()
                    stack.append(int(f*s))
                elif i=='/':
                    f=stack.pop()
                    s=stack.pop()
                    stack.append(int(s/f))
                else:
                    stack.append(int(i))
        return stack[0]