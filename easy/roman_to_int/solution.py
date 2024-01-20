from typing import List

class Solution:
    '''Forma mas o menos bruta
    def romanToInt(self, s: str) -> int:
        convert = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        calculate = convert[(s[-1])] # coger el ultimo elemento de s
        pre_element = calculate
        for element in reversed(s[:-1]): # empezar desde el penultimo, otra forma range(len(s)-2, -1, -1) -> (inicio, fin, paso)
            new_element = convert[element]
            if new_element < pre_element:
                calculate -= new_element
            else:
                calculate += new_element
            pre_element = new_element
        return calculate
    '''

    # 1 option for best solution, for with zip (take 2 elements), it can take more memory
    def romanToInt(self, s: str) -> int:
        convert = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        calculate = convert[(s[-1])] # we need the last element
        for current, next_ in zip(s[:-1], s[1:]): # current take from the first to the penultimate, next take from the second to the last
            if(convert[current] < convert[next_]):
                calculate -= convert[current]
            else:
                calculate += convert[current]
        return calculate


    ''' 2 option for best solution probably the best
    def romanToInt(self, s: str) -> int:
        convert = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        calculate = 0
        for element in range(len(s)):
            if element < len(s)-1 and convert[s[element]] < convert[s[element + 1]]:
                calculate -= convert[s[element]]
            else:
                calculate += convert[s[element]]
        return calculate
    '''