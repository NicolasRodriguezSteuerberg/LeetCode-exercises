# ENUNCIADO
Dada una cadena `s` que contiene solo los caracteres '(', ')', '{', '}', '[' y ']', determina si la cadena de entrada es válida.

Una cadena de entrada es válida si:

- Los paréntesis, corchetes y llaves abiertos deben cerrarse con el mismo tipo de paréntesis, corchetes y llaves, respectivamente.
- Los paréntesis, corchetes y llaves abiertos deben cerrarse en el orden correcto.
- Cada paréntesis, corchete o llave de cierre tiene un paréntesis, corchete o llave de apertura correspondiente del mismo tipo.

## QUE HE APRENDIDO?
Con este ejercicio he aprendido a como funcionan las pilas. En python las pilas se pueden implementar utilizando una lista. La pila sigue el principio de que el último en entrar es el primero en salir `metodo LIFO`.
Se pueden realizar operaciones como agregar un elemento en la parte superior de la pila llamado `"push"` esto se hace con la función append(). 
Otra operacion es la de quitar un elemento de la parte superior `pop`, se hace con la función pop(). Tambien puedes coger el último elemento sin eliminarlo con [-1] (nombrePila[-1])

Ejemplo de uso de una pila:
````python
# Crear una pila vacía
stack = []

# Push: agregar elementos a la pila
stack.append(1)
stack.append(2)
stack.append(3)

print("Pila después de agregar elementos:", stack)

# Pop: quitar el elemento superior de la pila
removed_element = stack.pop()
print("Elemento removido de la pila:", removed_element)
print("Pila después de hacer pop:", stack)
````
Imprimiirá esto:
````yaml
Pila después de agregar elementos: [1, 2, 3]
Elemento removido de la pila: 3
Pila después de hacer pop: [1, 2]
````