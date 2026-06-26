class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpendict = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        for c in s:
            if c in closeOpendict:
                if stack and stack[-1] == closeOpendict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False 
        