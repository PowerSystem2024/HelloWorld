//Array o Arreglos
//let autos = new Array('Ferrari', 'Renault', 'BMW'); Forma vieja

const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos);

//Recorremos los elementos de un arreglo
for(let i = 0; i < autos.length; i++);{
    console.log(i+' : ' +autos[i]);
}

//Modificamos los elementos del arreglo
autos[1]='Volvo';
console.log(autos[1]);

//Agregamos nuevos valores del arreglo
autos.push('Audi');
console.log(autos);
// Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Porche';
console.log(autos);
// Tercera forma de agregar elementos teniendo CUIDADO
autos[6]='Renault';
console.log(autos);
//Como preguntar si es un array o arreglo
console.log(Array.isArray[autos]);// Devuelve un booleano
// Segunda forma de preguntar si es un array
console.log(autos instanceof Array);// Pregunta si la variable es una instancia de la clase array y tambien devuelve un booleano