//Ejercicio-1: Iterar un rango de 0 a 10 e imprimir numeros divisibles por 3
console.log('Ejercicio-1')
for (let i = 0; i < 11; i++) {
    if (i%3==0) {
        console.log(i);
    }
}

//Ejercicio-2: Crear un rango de 2 a 6 
console.log('Ejercicio-2')
for (let i = 2; i < 7; i++) {
    console.log(i);
}
//Ejercicio-3: Crear un rango de 3 a 10 pero con incrementos de 2 en 2
console.log('Ejercicio-3')
for (let i = 3; i < 11; i+=2) {
    console.log(i);
}
//Ejercicio-4:Dada la siguiente tupla:
//tupla = (13,1,8,3,2,5,8)
//Crear una lista que solo incluya los numeros menores a 5
console.log('Ejercicio-4')
let lista1 = [13,1,8,3,2,5,8];
let lista2 = [];
for (let i = 0; i < lista1.length; i++) {
    if (lista1[i] < 5) {
        lista2.push(lista1[i]);
    }
}
console.log(lista2)