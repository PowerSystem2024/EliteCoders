//Esto se le conoce como hosting
miFuncion(8,2);

function miFuncion(a,b){

    //console.log("Sumamos: "+(a+b));
    return a + b ;
}

//nueva llamada a la funcion
miFuncion(5,4);

let resultado = miFuncion(6,7);
console.log(resultado);

//Declaramos una funcion de tipo expresion o anonima
let x = function(a,b){return a + b};
resultado= x( 5 , 6);//al llamarla se pone la variable y paraentesis
console.log(resultado);

//Funciones de tipo self y invoking
(Function (a,b));{
    console.log("Ejecutando la funcion: "+ (a + b));

}(9,6);

console.log(typeof miFuncion);
function miFuncionDos(a,b){
    console.log(arguments.length);
}

miFuncionDos(5,7,3,6);

//toString
var miFuncionTexto = miFuncionDos.toString()
console.log(miFuncionTexto);

//Funciones flecha
const summarFuncionFlecha = (a,b) => a + b;
resultado= summarFuncionFlecha(3,7);
console.log(resultado);

//Funcion tipo exprecion
let sumar = function(a = 4, b = 8){
    console.log(arguments[0]);
    console.log(arguments[1]);
    return a + b +arguments[2];

}
resultado=sumar(3,2,9)
console.log(resultado);

let respuesta = sumarTodo(5,4,13,10,9);
console.log(respuesta);
function sumarTodo(){
    let suma=0;
    for(let i = 0; i < arguments.length; i++ ){
        suma+= arguments[i];
    }
    return suma;
}

//Tipos prinitivos
let k =10;
function cambiarValor(a){
    a = 20;

}
cambiarValor(k);
console.log(k);

const persona={
    nombre:'Juan',
    apellido:'Lopez'
}
console.log(persona);

function cambiarValorObjeto(p1){
    p1.nombre='Ignacio';
    p1.apellido='Perez';
}

cambiarValorObjeto(persona);
console.log(k);