let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'maris@gmail.com',
    edad: 25,
    idioma: 'ES',
    
    // Getter para el idioma
    get lang() {
        return this.idioma.toUpperCase();
    },
    
    // Setter para el idioma
    set lang(lang) {
        this.idioma = lang.toUpperCase(); // Convierte las minúsculas a mayúsculas
    },
    
    // Método para el nombre completo
    nombreCompleto: function() {
        return this.nombre + ' ' + this.apellido;
    },
    
    // Getter para nombre y edad
    get nombreEdad() {
        return 'El nombre es: ' + this.nombre + ', edad: ' + this.edad;
    }
};

// Aquí comienza el código fuera del objeto
console.log("Comenzamos a utilizar el método get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el método get y set para idiomas");
persona.lang = 'en'; // Usamos el setter
console.log(persona.lang); 

function Persona3(nombre,apellido,email){
    this.nombre=nombre;
    this.apellido=apellido;
    this.email=email;
    this.nombreCompleto=function(){
        return this.nombre+' '+ this.apellido;
    }
}
let padre=new Persona3('Leo','Lopez','lopes@gmail.com');
padre.nombre='Luis';//modificamos el nombre
padre.telefono='26054650350165';//una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto());//utilizamos la funcion
let madre=new Persona3('Laura','Contrera','laura@gmail.com');
console.log(madre);
console.log(madre.telefono);//la propiedad no esta definida
console.log(madre.nombreCompleto());

//Diferecntes formas de crear objetos

//Caso objeto 1
let miObjeto=new Object();//Una opcion formal
//Caso objeto 2
let miObjeto2={};

//Caso strig 1
let miCadena1=new String('hola');//Sintaxis formal
//Caso strig 2
let miCadena2='hola';

//caso con numeros 1
let miNumero=new Number(1);
//caso con numeros 2
let miNumero2=1;

//Caso boolean 1
let miBoolean1=new Boolean(false);
//Caso boolean 1
let miBoolean2=false;


//caso arreglo 1
let miArreglo1=new Array();
//caso arreglo 2
let miArreglo2=[];

//Caso funtion 1
let miFuncion1=new function(){};//Todo despues del new es objeto
//Caso funtion 2
let miFuncion2=function(){};//Notacion simplificada y recomendad

//uso de prototype
Persona3.prototype.telefono='23565060323'
console.log(padre);
console.log(madre.telefono);
madre.telefono='2555421'
console.log(madre.telefono);

//uso de call
let persona4={
    nombre: 'juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+ this.nombre+' '+this.apellido+' '+ telefono;
       // return this.nombre+' '+this.apellido;
    }
}

let persona5= {
    nombre: 'Carlos',
    apellido: 'Lara',
}
console.log(persona4.nombreCompleto2('Lic.','1341653213'));
console.log(persona4.nombreCompleto2.call(persona5,'Ing.', '655465164'));

//Metodo apply
let arreglo=['Ing.','3236546515']
console.log(persona4.nombreCompleto2.apply(persona5,arreglo));

