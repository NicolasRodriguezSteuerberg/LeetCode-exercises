# ENUNCIADO
Dado un array de números enteros ordenados en orden no decreciente, elimina los duplicados in situ de manera que cada elemento único aparezca solo una vez. El orden relativo de los elementos debe mantenerse igual. Luego, devuelve el número de elementos únicos en nums.

Para ser aceptado, debes realizar las siguientes acciones:

Cambiar el array nums de manera que los primeros k elementos de nums contengan los elementos únicos en el orden en que estaban presentes en nums inicialmente. Los elementos restantes de nums no son importantes, al igual que el tamaño de nums.
Devolver k.

El juez probará tu solución con el siguiente código:
````python
int[] nums = [...]; // Arreglo de entrada
int[] expectedNums = [...]; // La respuesta esperada con la longitud correcta

int k = removeDuplicates(nums); // Llama a tu implementación

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
````
## QUE HE APRENDIDO?
Que si quieres añadir todos los elementos de un array a otro puedes hacerlo con la función ``extend(nombreLista)``. (No es muy eficiente)
