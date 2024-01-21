from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dummy = digits
        i = -1
        lenght = -len(digits) # todas las posiciones que voy a recorrer
        if dummy[i]==9:
            if i != lenght:
                while dummy[i] == 9 and i>=lenght:
                    if i==lenght and dummy[i]==9:
                        dummy[i] = 1
                        dummy.append(0)
                    elif i==lenght and dummy[i]!=9:
                        dummy[i] = dummy[i] + 1
                    else:
                        dummy[i] = 0
                        if dummy[i-1]!=9:
                            dummy[i-1] = dummy[i-1] + 1
                            break
                    i -= 1
            else:
                dummy[i] = 1
                dummy.append(0)
        else:
            dummy[i] = dummy[i] + 1
        return dummy