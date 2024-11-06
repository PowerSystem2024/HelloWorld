miFuncion(8, 2); // Esto se le conoce como hosting.
//Es el comportamiento donde las declaraciones de variables se mueven automaticamente al pricipio de su bloque de codigo antes de que se ejecute.

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a+b));
    return a + b;

}
//Llamamos le funcion
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);

//Declaramos una funcion de tipo expresion o anonima
let x = function(a, b){return a + b};//Necesita cierre con punto y coma
resultado = x(5, 6);// Al llamarla se pone la variable y el parentesis
console.log(resultado);

//Funciones tipo self e invoking
(function(a, b){
    console.log("Ejecutando la funcion: "+ (a + b));
})(9, 6);

console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.length);//no se puede utilizar fuera del bloque de la funcion
}

miFuncionDos(5, 7, 3, 6);

//toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

//Funcion flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7);
console.log(resultado)

// Funcion de tipo Expresion
let sumar = function (a = 4, b = 8){
    console.log(arguments[0]);// Muestra el parametro de : a 3
    console.log(arguments[1]);// Muestra el parametro de: b 6
    //console.log(arguments[2]);
    return a + b + arguments[2];
}
resultado = sumar(3, 2, 9);
console.log(resultado);


//Sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments [i]; // arguments es para arreglos
    }
     return suma;
}

//tipos primitivos
let k = 10;
function cambiarValor(a) {
    a = 20;
}
cambiarValor(k);
console.log(k);

//Paso por Referencia
const persona = {
    nombre: "Juan",
    apellido: "Lepez"
}
console.log(persona); 

function cambiarValorObjeto(p1){
    p1.nombre = "Ignacio";
    p1.apellido = "Perez";
}
cambiarValorObjeto(persona);
console.log(persona);