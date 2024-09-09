//Tarea: Todos los ejercicio hechos en otros lenguajes
// traerlos aquí con la sintaxis de JavaScript, por supuesto ejercicios de ciclos.


// Ejercicio 1
//Recorrer una lista

let lista=[1,2,2,3,4,5,6,7,8,9,10];
for (i in lista){
    
    console.log(i);         
   
         
}    

console.log("Se acabaron los elementos de la lista");

//Ejercice 2:
//Iterar un rango de 0 10 e imprimir numeros divisibles entre 3

for (let i=0; i < 10; i++  ){

    if (i % 3==0){
        console.log(i);
    }
    


}
   

   //Ejercice 3 :
//Crear un rango de numeros de 2 a 6 e imprimilos

numList=[1,2,3,4,5,6,7,8];
for (i in numList){
    
    if(i<2 || i > 6 ){
        
        continue;
        
    }
       
    else{
        
       console.log(i);
    }
    
}
    

// Ejercice 4:
//Crear un rango de 3 a 10 pero con incremento de 2 en 2.

for (i= 0; i < 11; i+=2 ){
    
    console.log(i);
    
    
}

//Costo pero funciono!!!





















