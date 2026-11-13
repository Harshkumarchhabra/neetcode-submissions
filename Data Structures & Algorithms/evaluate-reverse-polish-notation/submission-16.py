class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if len(stack)>=2:
                if i=='+':
                    a=stack.pop()
                    b=stack.pop()
                    val=int(a)+int(b)
                    stack.append(val)
                elif i=='-':
                    a=stack.pop()
                    b=stack.pop()
                    val=int(b)-int(a)
                    stack.append(val)
                elif i=='*':
                    a=stack.pop()
                    b=stack.pop()
                    val=int(a)*int(b)
                    stack.append(val)
                elif i=='/':
                    a=stack.pop()
                    b=stack.pop()
                    val=int(int(b)/int(a))
                    stack.append(val)
                else:
                    stack.append(int(i))
            else:
                stack.append(int(i))
        return stack[-1]