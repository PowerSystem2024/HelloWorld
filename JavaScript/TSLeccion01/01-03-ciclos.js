// ciclo while

let contador = 0
while(contador < 3) {
    console.log(contador);
    contador++;
}

console.log('Fin del ciclo while');

// Do While

let conteo = 0;
do {
    console.log(conteo);
    conteo++;
} while (conteo < 3);

console.log('Fin del ciclo do while');

// Ciclo For

for(let contando = 0 ;contando < 3 ; contando ++){
    console.log(contando);
}
console.log('Final del ciclo For');

//Palabra Reservada Break
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 == 0) {
        console.log(contando);
        break;
    };
    
}
console.log('Termina el cilco al encontrar el primer numero par');

// Palabra continue
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 !== 0) {
        continue;
        
    };
    console.log(contando);
    
}
console.log('Termina el cilco');

//La palabra continue y Etiquetas Laber
inicio: 
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 !== 0) {
        continue inicio;
        
    };
    console.log(contando);
    
}
console.log('Termina el cilco con la etiqueta Label');