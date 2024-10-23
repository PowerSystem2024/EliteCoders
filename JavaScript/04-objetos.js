let x = 10; //variable de tipo primitiva
console.log(x.length);
console.log('Tipos Primitivos');
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: '30',
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase(); //Convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){//metodo o funcion en JavaScript
        return this.nombre + ' ' + this.apellido;
    },
    get nombreEdad(){//Este es el metodo get
        return 'El nombre es; '+this.nombre+' edad: '+this.edad;
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

console.log('Comenzamos a usar el metodo get');
console.log(persona.nombreEdad);

console.log('Comenzamos a usar el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){//Constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre + ' ' + this.apellido;
    }
}
let padre = new Persona3('Leo', 'Lopez', 'lopez@gmail.com');
padre.nombre = 'Luis';//Modificamos el nombre
padre.telefono = '5492618282821';
console.log(padre);
console.log(padre.nombreCompleto());//Utilizamos la funcion
let madre = new Persona3('Laura', 'Contrera', 'contrera@gmail.com');
console.log(madre);
console.log(madre.telefono);//la propiedad no esta difinida
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos

//Caso objeto 1
let miObjeto = new Object(); //esta es una opcion formal
//Caso objeto 2
let miObjeto2 = {};//Esta opcion es breve y recomendada

//Caso String 1
let miString = new String('Hola');//Sintaxis formal
//Caso String 2
let miString2 = 'Hola';//Esta es la sintaxis simplificada y recomendada

//Caso Number 1
let miNumero = new Number(5);//Es formal no recomendable
//Caso Number 2
let miNumero2 = 5;//Esta es la sintaxis simplificada y recomendada

//Caso Boolean 1
let miBoolean = new Boolean(true);//Es formal no recomendable 
//Caso Boolean 2
let miBoolean2 = true;//Esta es la sintaxis simplificada y recomendada

//Caso arreglos 1
let miArreglo = new Array();//Es formal no recomendable
//Caso arreglos 2
let miArreglo2 = [];//Esta es la sintaxis simplificada y recomendada

//Caso Funcion 1
let miFuncion1 = new function(){};//Todo despues de new es considerado objeto
//Caso Funcion 2
let miFuncion2 = function(){}//Esta es la sintaxis simplificada y recomendada

//Uso de prototype
Persona3.prototype.telefono = '2618383832';
console.log(padre);
console.log(madre.telefono);
madre.telefono='5492618383832';
 console.log(madre.telefono);

//Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+' '+this.nombre+' '+this.apellido+' '+telefono;
        //return this.nombre+' '+this.apellido;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic.', '5492618484845'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '5492618585856'));

//Metodo Apply
let arreglo = ['Ing.', '5492618686865'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));