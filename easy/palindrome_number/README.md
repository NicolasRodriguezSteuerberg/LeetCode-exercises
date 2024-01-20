# Enunciado
Dado un numero retorna True si x es capicua, si no que devuelva falso
<details>
    <summary><b>RETO</b></summary>
    <p>
    Serias capaz de resolverlo sin convertirlo a String
    </p>
</details>

## Que he aprendido
1. Primero de todo he aprendido que se puede invertir un string simplemente usando [::-1]
2. Segundo que si es un numero negativo o un multiplo de 10 nunca van a ser capicua
3. Que simplemente tenemos que coger la primera mitad y la mitad del final para compararlo
    
   - Para esto tenemos que tener en cuenta que puede ser impar por lo que tambien hay que poner una condicion para quitarle el ultimo digito al numero que mas digitos tenga
4. Que para ir cogiendo el último digito de un numero llega con coger el resto de la division de un numero entre 10
5. Que si queremos quitarle el último digito a un número solo tenemos que coger el cociente de dividirlo entre 10 (// -> signo para hacerlo)
6. 