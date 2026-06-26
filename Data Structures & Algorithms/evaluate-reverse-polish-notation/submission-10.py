class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calStack = []
        for token in tokens:
            if token == "+":
                a, b = calStack.pop(), calStack.pop()
                calStack.append(a + b)
            elif token == "-":
                a, b = calStack.pop(), calStack.pop()
                calStack.append(b - a)
            elif token == "*":
                a, b = calStack.pop(), calStack.pop()
                calStack.append(a * b)
            elif token == "/":
                a, b = calStack.pop(), calStack.pop()
                calStack.append(int(float(b) / a)) 
            else: 
                calStack.append(int(token))
        return calStack[0]
                

                 
        