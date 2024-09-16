//ciclo while
let contador= 0;
while (contador < 3){
    console.log(contador);
    contador++;

}
console.log("fin del ciclo while");

//DO WHILE
let conteo = 0;
do{
    console.log(conteo);
    conteo++;

}while(conteo < 3);

console.log("fin del ciclo do while");

//FOR

for(let contando = 0; contando < 3; contando ++){
    console.log(contando);
}
console.log("fin del ciclo For");


// Break
for(let contando = 0; contando <= 10; contando ++){
   
    if(contando % 2 == 0){
        
        console.log(contando);
        break
        
    }
    
}
console.log("Termina el ciclo al encontrar el primer numero  par");

//LA Palabra CONTINUE y Eriquetas Labels

inicio:
for(let contando = 0; contando <= 10; contando ++){
   
    if(contando % 2 != 0){
        
        continue inicio;//sigue con la iteracion(vuelve al ciclo for sin hacer otra cosa)

    }
    console.log(contando)

}
console.log("Termina el ciclo ");





