let x = 10;
console.log(x.length);
console.log('Tipo Primitivo');

// Objeto
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30,
    nombreCompleto: function(){// Metodo o funcion en JavaScript
        return this.nombre + " "+ this.apellido;

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

