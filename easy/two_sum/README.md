# Enunciado
Dada una lista de numeros enteros devuelve una lista de enteros con los indices de la primera lista, el valor de la
## Que usé
En este ejercicio usé una hash table, específicamente implementando una hash table utilizando un diccionario
## COSAS NUEVAS QUE HE APRENDIDO
### Facilidad para buscar cosas en un diccionario
Es más fácil buscar si existe una llave que si existe un valor:
````python3
diccionario = {
    23 : 1,  # key : value
    24 : 2,
    
} 
# buscar una llave
key = 23
key in diccionario # esto devuelve un booleano
# buscar un valor
value = 2
value in diccionario.values()
````
A parte de esa diferencia si quieres solo tener un valor igual te llega con ponerlo como llave, de esta manera si intentas añadir otro con la misma llave lo sobreescribirá, por lo que si quieres que no se sobreescriba tendrás que hacer un if, puedes hacerlo de dos maneras:
````python
diccionario = {
    23 : 1,  # key : value
    24 : 2,
    
} 
clave_nueva = 23
valor_nuevo = 3
# primera forma
if clave_nueva not in diccionario:
     diccionario[clave_nueva] = valor_nuevo
# segunda forma
if diccionario.get(clave_nueva) is None:
    diccionario[clave_nueva] = valor_nuevo
````

### FUNCION HASH TABLES
#### QUE ES?
 Una `hash table` es una estructura de datos que implementa una asociación de  claves a valores (en python un diccionario utiliza la hash table, en otros lenguajes no funciona asi el diccionario).
Funciona mediante el uso de una función hash para calcular un índice en el cual se almacena oñ busca el valor asociado con la clave. La funcion hash toma la clave como entrada y produce un valor numérico(hash code), que se utiliza para determinar la ubicación de almacenamiento en la tabla.

Las hash tables son eficientes para búsquedas, inserciones y eliminaciones en promedio, ya que la búsqueda y la actualización tienen una complejidad de tiempo O(1) en el caso ideal. Sin embargo, en el peor caso, si hay muchas colisiones, la complejidad puede aumentar, aunque las estrategias de manejo de colisiones están diseñadas para minimizar este problema.


**Funciones:**

1. **Función Hash:**
   - Convierte la clave en un valor numérico.
   - Busca distribuir uniformemente las claves para reducir colisiones.

2. **Índice de Almacenamiento:**
   - Utiliza el valor hash como índice en la tabla hash.
   - Determina la ubicación para almacenar o buscar el valor asociado con la clave.

3. **Colisiones:**
   - Ocurren cuando dos claves generan el mismo valor hash.
   - Estrategias comunes: encadenamiento (chaining) y direccionamiento abierto.

    a. **Encadenamiento (Chaining):**
       - Cada celda contiene una lista de elementos con la misma posición hash.
       - En caso de colisión, los elementos se añaden a esta lista.

    b. **Direccionamiento Abierto:**
       - En caso de colisión, busca la siguiente posición vacía para almacenar el valor.
       - Estrategias incluyen sondeo lineal, cuadrático y doble dispersión.

4. **Búsqueda y Actualización:**
   - Para buscar un valor, se aplica la función hash, se encuentra la posición y se recupera el valor asociado.
   - Para actualizar o insertar, se sigue el mismo proceso.
