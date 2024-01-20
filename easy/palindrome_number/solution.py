class Solution:
    '''Manera convirtiendolos en string
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        return x == int(str(x)[::-1]) # un string se puede poner al reves gracias a [::-1]
    '''

    '''Manera sin convertirlos en string
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Los números negativos no son palíndromos
        original = x
        reversed_num = 0 # se pone a 0 para que asi el primer digito añadido solo sea un digito y no 11 por ejemplo

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit # multiplica x 10 para añadirle un cero y poder añadir el nuevo digito
            x = x // 10 # va bajando una cifra(12312 la siguiente pasa a 1231), asi cuando no tenga mas va a ser 0 y saldra del while

        return original == reversed_num
    '''

    '''Mejor manera sin convertirlos en string es comparando solo la mitad de la cadena'''

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0): # descartamos los que son negativos y los numeros que acaban en 0
            return False
        reversed_num = 0

        while x > reversed_num: # de esta manera solo comparamos la mitad
            reversed_num = reversed_num * 10 + x % 10 # aumentamos un digito cogiendo el resto de dividir un numero por 0
            x //= 10 # le quitamos el ultimo digito // -> coge el cociente (entero) de la division, al dividir entre 10 siempre va a dar el mismo numero quitando el ultimo

        return x == reversed_num or x == reversed_num // 10 # el or es para poder comparar los numeros impares
