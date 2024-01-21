En este repositorio estoy subiendo los ejercicios que voy haciendo en leetCode para estudiar/practicar conceptos nuevos. 
En cada carpeta de ejercicios contiene un readme donde me explico a mi mismo o a personas como tu que ven esto cosas que yo he aprendido haciendolos/cosas
que podrian servirte de ayuda para intentar hacer los ejercicios con conceptos que a lo mejor no sabias.

Si haceis el ejercicio de una manera bastante mas eficiente me gustaria que me lo mandarais para comparar y saber otras maneras de hacer estos ejercicios
1. [EASY](easy)


# BIG O
La notación BIG O es una forma de describir el rendimiento de un algoritmo en términos de como se comporta a medida que aumenta el tamaño de la entrada `input`.
Se utiliza para analizar la eficiencia temporal de un algoritmo, es decir como varía el tiempo de ejecución en función del tamaño del conjunto de datos de entrada.

La notación Big O se representa normalmente como `O(f(n))` donde *f(n)* es una función que describe la tasa de crecimiento del algoritmo en relación con el tamaño de la entrada *n*. Existen algunas categorías comunes:
1. **O(1) - Constant Time**
   - Indica que el tiempo de ejecución no depende del tamaño de la entrada.
     - Acceder a un elemento específico en un array/lista mediante su índice
     - Insertar o eliminar un elemento en la primera posición de una lista vinculada de longitud fija
     - push() / pop() en una pila
     - Operaciones matemáticas
     - Accediendo a un hash a través de su key(llave)
     - Retornar un valor en una funcion
     
2. **O(log(n)) - Logarithmic time**
   - La complejidad aumenta logarítmicamente con el tamaño de la entrada. 
   Los algoritmos con esta complejidad suelen dividir el conjunto de datos en partes más pequeñas en cada iteración.
     - Busquedas binarias en listas
       - While()?
     - Árboles de búsqueda binaria
3. **O(n) - Linear Time**
   - La complejidad es directamente proporcional al tamaño de la entrada. A medida que la entrada crece, el tiempo de ejecución también crece de manera lineal.
     - Recorrer una lista entera (con bucles generalmente)
       - 'Recorrer una lista para encontrar un elemento en específico' (es y no)
     - Sumar todos los elementos de una lista
     - Buscar el valor máximo o mínimo en una lista no ordenada

4. **O(n^2) - Quadratic Time**
   - Algoritmo de ordenacion
     - Bubble Sort
   - Busqueda exhaustiva de pares de elementos en una lista
     - 1 for dentro de otro

5. **O(2^n) - Exponential Time**
   - La complejidad crece de manera exponencial en función del tamaño del input
     - Algoritmos recursivos que generan todas las combinaciones posibles, como la generación de subconjuntos