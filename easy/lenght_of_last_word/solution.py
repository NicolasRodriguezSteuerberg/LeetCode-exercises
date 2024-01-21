from typing import List

class Solution:
    '''No es mala opcion
    def lengthOfLastWord(self, s: str) -> int:
        lista = s.split()
        return len(lista[-1])
    '''

    '''Mejor opcion que la anterior
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        letraEncontrada = False
        lenght = 0
        while(i >= 0):
            if s[i] == " " and not letraEncontrada:
                i -= 1
            elif s[i] != " ":
                lenght += 1
                i -= 1
            else:
                return lenght
        return lenght
    '''

    '''Mejor opcion que la anterior, 2 whiles que recorren lo mismo pero de manera diferente no hace que sea mas lento...'''
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        lenght = 0
        while i >= 0 and  s[i] == " ":
                i -= 1
        while i >= 0 and s[i] != " ":
            lenght += 1
            i -= 1
        return lenght