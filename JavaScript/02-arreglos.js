// let autos =new array('Ferrari','Renault','BMW'); esta es una sintaxis vieja fuera de uso
const autos = ['Ferrari','Renault','BMW'];
console.log(autos);

//Recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[1]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++){
    console.log(i+' : '+autos[i]);
}

//Modificamos los elementos de un arreglo
autos[1] = 'Volvo';
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push('Audi');
console.log(autos);

//Otras formas de agregar elementos
autos[autos.length] = 'Porche';
console.log(autos);

//Tercera forma de agregar elementos TENER CUIDADO
autos[6]='Fiat';
console.log(autos)

//Como preguntar si es un Array o arreglo
console.log(Array.isArray(autos)); //Nos devuelve true o false
//Otra forma
console.log(autos instanceof Array);//Se consulta si la variable es una instancia de Array
