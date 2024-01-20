from typing import List

class Solution:

    '''worst solution
    def isValid(self, s: str) -> bool:
        # dictionary to see if its open or close
        map = {
            "(": "open",
            "{": "open",
            "[": "open",
            ")": "close",
            "}": "close",
            "]": "close"
        }
        # dictionaty to see if its the correspondence bracket
        map2 = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = [] # we need to use a stack

        for element in s:
            if map[element] == "open": # if its open we put the element in the stack (on the top)
                stack.append(element)
            elif map[element] == "close" and len(stack)!=0: # if its close and the lenght of the stack its > 0
                if map2[element] == stack[-1]: # if the first element(top element) is the same to the open bracket
                    stack.pop() # we pop the top element of the stack
                else: # else we return false because we close without having the correspondece bracket
                    return False
        if len(stack) != 0: # return false if we only have an open bracket
            return False
        return True # if all okey return true
    '''

    '''Long version of the best
    def isValid(self, s: str) -> bool:
        # dictionary to see if its open or close
        map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        for element in s:
            if element in map: # if we have the element in the key we add it
                stack.append(element)
            elif element in map.values():
                if not stack or map[stack.pop()] != element:
                    return False             
    '''

    '''shortest version and best'''
    def isValid(self, s: str) -> bool:
        # dictionary to see if its open or close
        map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []

        for element in s:
            if element in map: # if we have the element in the key we add it
                stack.append(element)
            elif len(stack) == 0 or element != map[stack.pop]: # if the problem dont say just brackets: (len(stack) == 0 or element != map[stack.pop]) and element in map.values()
                # if we don't have elements in stack because we didnt have an open bracket
                # or if the close bracket (element) if not the same of the top element
                return False
        return len(stack) == 0