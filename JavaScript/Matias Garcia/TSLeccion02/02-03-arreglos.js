//Arreglos o Array
//Antigous
//let autos= new Array("Ferrari","Renaul","BMW")

//Asi se debe crear un arreglo
const autos=["Ferrari","Renaul","BMW"];
console.log(autos);

//Recorremos los elementos
console.log(autos[0]);
console.log(autos[2]);

for(let i=0; i < autos.length; i++){
    console.log(i+" : "+autos[i]);
}

//Modificamos los elementos del arreglo´
autos[1]='Volvo';
console.log(autos[1]);


//Agregamos nuevos elementos
autos.push('Audi');
console.log(autos);

//Otra forma de agregar
autos[autos.length]='Porche';
console.log(autos);

//Tercera forma de agregar(no recomendado)
autos[6]='Renaul';
console.log(autos);


//Como preguntar si es un arreglo o array
//devuelve un booleano
console.log(Array.isArray(autos));

//Preguntamos di la variable es  una instancua de ka ckase array
console.log(autos instanceof Array);


















