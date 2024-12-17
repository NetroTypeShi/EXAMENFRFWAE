# Teoria

Realiza el examen directamente sobre el archivo!

Este examen solo muestra algunos conceptos al azar que me parecen importantes, hay muchos!

Intenta añadir código cuando lo necesites utilizando

```lenguaje
codigo
```

1. ¿Que diferencia una variable creada con `let` de una creada con `const`?
const es para variables que no se pueden cambiar, es decir inmutables y let es para variables que se pueden cambiar.

2. ¿Qué es un dato primitivo? ¿y un objeto?
Son los datos originales de un lenguaje de programación. Los objetos son formas de representar conceptos de un programa.

2. ¿Qué diferencia hay entre `==` y `===`?
== (igualdad débil):
    Compara los valores después de hacer conversión de tipo (coerción de tipo) si los operandos son de tipos diferentes.
    Esto significa que, antes de comparar los valores, JavaScript puede convertirlos a un tipo común.
=== (igualdad estricta):
    Compara tanto los valores como los tipos de datos sin realizar ninguna conversión de tipo.
    Esto significa que ambos operandos deben ser del mismo tipo y tener el mismo valor para que la comparación sea verdadera.
3. Analiza el siguiente código, ¿qué valor se mostrará en la consola?

```js
let a = 1;

function mi_funcion() {
    let a = 2;
}

mi_funcion();
console.log(a);
```
Mostrará el valor 1 , ya que el código de console.log es para que se muestre algo en consola, más o menos como un print, este cogerá el valor general que es 1 y como el 2 está en una función a pesar de que se ejecute para mostrar el 2 debería tener un console.log(a) dentro de la función, pero como el console log está fuera cogerá el valor de a del que está afuera


4. ¿Qué es el DOM? Explícalo brevemente.
Interfaz de programación que tiene una estructura de un documento HTML como un árbol jerárquico

5. ¿Este código es correcto? Si no lo es, ¿por qué?
```js
const boton = document.querySelector('button')//busca un botón en el html y le da el valor a la variable boton;
function saluda() {
    console.log('Hola');//Crea una función en donde se imprime hola en la consola
}
boton.addEventListener('click', saluda());// Al detectar click realiza la función saluda()
```
Está bien el código de js pero eso sí que necesitará todo el resto de estructura html de atrás y además está cogiendo todos los button así que si hay más de un button no se diferenciará

6. ¿Que formas de seleccionar elementos del DOM conoces? ¿Cuál es la diferencia entre ellas?
7. ¿Qué es un evento? ¿Qué formas conoces de crearlos?
Un evento es cuando se interactúa con un objeto del resultado del código. boton.addEventListener('click', saluda())
8. ¿Como se añade una libreria externa a un proyecto de JavaScript? Puedes usar p5 como referencia.
9. ¿Que es esto? `<meta charset="UTF-8">` ¿Por qué es importante?
Se trata de una etiqueta que define la codificación de algun elemento HTML. Sirve para evitar errores y problemas con algunos caracteres que sean "especiales" y no pueda detectarlos bien
10. ¿Que es una función? Explica brevemente su sintaxis en el lenguaje que prefieras.
Es un conjunto de código o boque de código, el cuál se puede acceder de manera cómoda sin tener que repetir todo el código

Ejemplo unity:
```c#
void (talkaLittlebit) // nOMBRE DE LA FUNCIÓN
{
 print ("Hello dawg"); // Esto lo imprime en la consola un "Hello dawg"
}

void update()
{
 talkaLittlebit(); // Ejecuta la función en update, es decir cada frame
}
```