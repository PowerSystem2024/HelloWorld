class Persona {
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

}

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
//console.log(persona1);
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);
//console.log(persona2);
//*****EJERCICIO*****
//Crear el método get y set para el atributo de apellido, 
//luego modificar el apellido a través del  set y mostrar con un console.log 
//lo que es el get donde muestra el resultado obtenido.
let persona = {
    nombre: 'Juan',
    _apellido: 'Perez',  // Usamos un guion bajo para diferenciar la propiedad privada

    // Método get para obtener el apellido
    get apellido() {
        return this._apellido;
    },

    // Método set para modificar el apellido
    set apellido(nuevoApellido) {
        this._apellido = nuevoApellido;
    }
};

// Modificar el apellido a través del set
persona.apellido = 'Gomez';

// Mostrar el apellido actualizado usando el get
console.log(persona.apellido);  // Salida: Gomez



