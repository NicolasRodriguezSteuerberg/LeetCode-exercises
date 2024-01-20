# ENUNCIADO

# QUE HE APRENDIDO?
## Que es una ListNode
Una ListNode es una estructura de datos utilizada para implementar listas enlazadas `estructura de datos lineal`.
Una lista enlazada es una colección de nodos, donde cada nodo contiene un valor y una referencia `enlace` al siguiente nodo en la secuencia.
La última referencia de un nodo suele ser "None", esto indica que es el final de la lista
### Como funcionan?
#### Estructura básica
````python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
````
Aquí `value` es el valor almacenado en el nodo, mientras que next es la referencia al otro nodo.

#### Ejemplo sencillo de tres nodos
````python
# tenemos que crear la clase listNode
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
# creamos la lista de nodos
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Establecemos las referencias
node1.next = node2
node2.next = node3
# no es necesario poner el next del nodo3 por que por defecto es None

# La lista enlazada comienza en el nodo 1
head = node1

# si quisieramos ver el 3 nodo (es mejor hacer comprobaciones de que existe el nodo)
print(head.next.next)
````
Si con este ejemplo quisieramos eliminar el último por que no podriamos cambiar que el ultimo apunte al anterior. Si quisieramos eliminar el nodo 2

## Que es Optional?
Optional es un tipo proporcionado por el módulo typing de Python que indica que un valor puede ser de un tipo específico o None

## TERMINOLOGIA DUMMY
En programación el término `dummy` se utiliza para referirse a algo que no tiene valor real o significado, si no que se utiliza temporalmente o como marcador de posición.
Generalmente se utiliza par indicar un valor o identidad que no es importante o relevante para la lógica principal, sino que se utiliza solo con fines prácticos o de estructuración del código.

En el código del ejercicio dummy se utiliza como nodo ficticio (1 nodo es vacio)