class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
                if stack and tokens[i]=="+":
                    one=stack.pop()
                    two=stack.pop()
                    calc=one + two
                    stack.append(calc)
                elif stack and tokens[i]=="-":
                    one=stack.pop()
                    two=stack.pop()
                    calc=two-one
                    stack.append(calc)
                elif stack and tokens[i]=="*":
                    one=stack.pop()
                    two=stack.pop()
                    calc=one * two
                    stack.append(calc)
                elif stack and tokens[i]=="/":
                    one=stack.pop()
                    two=stack.pop()
                    calc=int(two/one)
                    stack.append(calc)
                else:
                    stack.append(int(tokens[i]))
        return stack[-1]