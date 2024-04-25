class Solution(object):
    def isValid(self, s):
        stack = []
        map = {")": "(", "}": "{", "]": "["}
    
        for char in s:
            if char in map:
                top = stack.pop() if stack else '#'
                if map[char] != top:
                    return False
            else:
                stack.append(char)
    
        return not stack
    



  

