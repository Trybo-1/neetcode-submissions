class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '['}

        for item in s:
            if item in matching:
                if len(stack) != 0 and stack[-1] == matching[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        
        if len(stack) != 0:
            return False
            
        return True