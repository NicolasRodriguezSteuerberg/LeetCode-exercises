# Enunciado
Los números romanos se representan mediante siete símbolos diferentes: I, V, X, L, C, D y M.

| Símbolo | Valor |
| ------- | ----- |
| I       | 1     |
| V       | 5     |
| X       | 10    |
| L       | 50    |
| C       | 100   |
| D       | 500   |
| M       | 1000  |

Por ejemplo, el 2 se escribe como II en números romanos, simplemente se suman dos unos. El 12 se escribe como XII, que es simplemente X + II. El número 27 se escribe como XXVII, que es XX + V + II.

Los números romanos suelen escribirse de mayor a menor de izquierda a derecha. Sin embargo, el numeral para el cuatro no es IIII. En su lugar, el número cuatro se escribe como IV. Debido a que el uno está antes del cinco, se resta, haciendo cuatro. El mismo principio se aplica al número nueve, que se escribe como IX. Hay seis instancias en las que se utiliza la resta:

- I puede colocarse antes de V (5) y X (10) para hacer 4 y 9.
- X puede colocarse antes de L (50) y C (100) para hacer 40 y 90.
- C puede colocarse antes de D (500) y M (1000) para hacer 400 y 900.

Dado un número romano, conviértelo a un entero.

## COSAS QUE HE APRENDIDO
### QUE ES ZIP EN PYTHON Y COMO FUNCIONA
`Zip` es una función de python que toma dos o más iterables como listas o cadenas y los combina en pares. Cada par contiene los valores de la misma posicion correspondientes a las iteraciones originales:
```python
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

pares = zip(lista1, lista2)

for par in pares:
    print(par) # (1, "a"), (2, "b"), ...
```
Tambien puedes hacerlo con la misma cadena de texto o lista:
```python
texto = "12345"

pares = zip(texto[:-1], texto[1:])
# texto[:-1] cogeria todos los valores menos el último, en cambio
# textp[1:] cogería todos los valores excepto el primero
for par in pares:
    print(par) # ("1", "2"), ("2", "3")
```
Esto último lo puedes usar para recorrer un for de manera que te devuelva 2 elementos
````python
s = "ABCDEF"
for current, next_ in zip(s[:-1], s[1:]):
    print(current, next_) # ("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F")
````
De esta manera he usado el zip para hacer el ejercicio:
````python
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
    for current, next_ in zip(s[:-1], s[1:]): 
        # current take from the first to the penultimate
        # next take from the second to the last
        if(convert[current] < convert[next_]):
            calculate -= convert[current]
        else:
            calculate += convert[current]
    return calculate
````
He tenido que inicializar la acumulacion de la calculacion con el último elemento por que si no no llegariamos a sumar ese elemento, se podria hacer al final pero es insignificante cuando lo hagas, por lo que si lo haces al principio te ahorras una linea de codigo