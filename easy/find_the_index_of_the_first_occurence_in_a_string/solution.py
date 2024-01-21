from typing import List

class Solution:
    ''''''
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle) # si no lo encuentra devuelve -1 si lo encuentra devuelve la posición de donde empieza (si hay 2 devuelve la 1)

    '''
    hello -> 5
    ll -> 2
    5 - 2 + 1 = 4
    '''

    '''More eficient'''
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for i in range(len(haystack) - len(needle)):
                if haystack[i: i + len(needle)] == needle:
                    return i
        return -1
