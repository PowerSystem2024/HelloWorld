//let persona3 = new Persona('Carla', 'Ponce');

class Persona {//Clase padre
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
    get apellido(){
        return this._ap
        
        ellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    nombreCompleto(){
        return this._nombre+' '+this._apellido;
    }
}

class Empleado extends Persona{//Clase Hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }
    //SobreEscritura
    nombreCompleto(){
        return this._nombre+' '+this._apellido+' '+this._departamento;
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

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());