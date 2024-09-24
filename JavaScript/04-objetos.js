let x = 10; //variable de tipo primitiva
console.log(x.length);
console.log('Tipos Primitivos');
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: '30',
    nombreCompleto: function(){//metodo o funcion en JavaScript
        return this.nombre + ' ' + this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');
let persona2 = new Object();//Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '123456789';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');
console.log(persona['apellido']);//Accedemos como si fuerea un arreglo
console.log('Usamos el ciclo for in');
//For in y accedemos al objeto como si fuera un arreglo
for(let propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}
console.log('Cambiamos y eliminamos un error');
persona.apellida = 'Betancud';//Cambiamos dinamicamente un valor del objeto
delete persona.apellida;//Eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
console.log('Distintas formas de imprimir un objeto');
//Numero 1: (la mas sencilla) concatenar cada valor de cada propiedad
console.log('Forma 1');
console.log(persona.nombre + ' ' + persona.apellido);
//Numero 2: A travez del ciclo for in
console.log('Forma 2');
for(let propiedad in persona){
    console.log(persona[propiedad]);
}
//Numero 3: La funcion Object.values()
console.log('Forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);
//Numero 4: Utilizaremos el metodo JSON.stringify()
console.log('Forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);