let x = 10;
console.log(x.length);
console.log('Tipo Primitivo');

// Objeto
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 28,
    idioma: 'ESPAÑOL',
    get lang(){
        return this.idioma.toUpperCase();// Convierte las minusculas en mayusculas.
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){// Metodo o funcion en JavaScript
        return this.nombre + " "+ this.apellido;

    },
    get nombreEdad(){//Este es el metodo Get
        return 'El nombre es: '+this.nombre+', Edad:  '+this.edad;
    }
    
}

console.log(persona.nombre);
// Objeto parte 2
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());

let persona2 = new Object();//Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion ='Salada 14'
persona2.telefono = '5492618282821';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto')
console.log(persona['apellido']);//Accedemos como si fuera un arreglo
console.log('Usamos el ciclo for in');
//For in y accedemos al objeto como si fuera un arreglo
for (propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]); 
}
console.log('Cambiamos y modificamos un error');
persona.apellido = 'Bentancud'; //Cambiamos dinamicamente un valor del objeto
delete persona.apellida;//Eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
//Numero 1: La mas sencilla: concatenar cada propiedad
console.log('Distintas formas de imprimir un objeto: Form 1')
console.log(persona.nombre+' '+persona.apellido);
//Numero 2: A traves del ciclo for in
console.log('Distintas formas de imprimir un objeto: Form 2')
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}
//Numero 3: La funcion Objet.values()
console.log('Distintas formas de imprimir un objeto: Form 3')
let personaArray = Object.values(persona);
console.log(personaArray);
//Numero 4: Utilizaremos el metodo JSON.stringify
console.log('Distintas formas de imprimir un objeto: Form 4')
let personaString = JSON.stringify(persona);
console.log(persona);

console.log('Comenzamos a utilizar el metodo Get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idioma');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Leo', 'Lopez', 'lopezl@gmail.com');
padre.nombre = 'Luis';//modificamos el nombre
padre.telefono = '5492618282821';
console.log(padre);
console.log(padre.nombreCompleto());//utilizamos la funcion

let madre = new Persona3('Laura', 'Contrera', 'contreral@gmail.com');
console.log(madre);
console.log(madre.telefono);//La propiedad no esta definida
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos
//casi numero 1
let miObjeto = new Object();
//caso numero 2
let miObjeto2 = {};

//caso String
let miCaddena1 = newString('Hola');//Sintaxis formal
//caso String 2
let miCadena2 = 'Hola'//Sintaxis simplificada y recomendada

//caso numero 1
let miNumero = new Number(1);// Es formal no recomendable
let miNumero2 = 1;//Sintaxis recomendada

//caso boolean 1
let miBoolean1 = new Boolean(false);//Formal
//caso boolean 2
let miBoolean2 = false; // Sintaxis recomendada

//Casos Arreglos 1
let miArreglo1 = new Array();//Formal
let miArreglo2 = [];//Sintaxis recomendada

//Funciones caso 1
let miFuncion1 = new function(){};// Todo despues del new es considerado objeto
//caso 2
let miFuncion2 = function(){};//Notacion simplificada y recomendada

//Uso de prototype
Persona3.prototype.telefono = '2618383832';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '5492618383832'

//Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        //return titulo+' '+this.nombre+' '+this.apellido;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic.', '5492618383834'));
console.log(persona4.nombreCompleto2.call(persona5, ' Ing.', '5492618585856'))

//Metodo Apply
let arreglo = ['Ing.', '5492618686865'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));