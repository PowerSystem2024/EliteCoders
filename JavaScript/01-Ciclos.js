//While
let contador = 0;
while (contador < 3) {
    console.log(contador);
    contador++;
}
console.log("Fin del ciclo while");

//Do while
let conteo = 0;
do {
    console.log(conteo);
    conteo++;
} while (conteo < 3);
console.log("Fin del ciclo do while");

//For
for (let contando =0; contando < 3; contando++){
    console.log(contando);
}
console.log("Fin del ciclo for");

//Break
for (let contando =0; contando < 10; contando++){
    if (contando % 2 == 0){
        console.log(contando);
        break;
    }
}
console.log("Termina el ciclo al encontrar el primer numero par");

//Continue
for (let contando =0; contando <= 10; contando++){
    if (contando % 2 !== 0){
        continue;
    }
    console.log(contando);
}
console.log("Termina el ciclo");

//Etiquetas
inicio:
for (let contando =0; contando < 10; contando++){
    if (contando % 2 == 0){
        console.log(contando);
        break inicio;
    }
}
console.log("Termina el ciclo al encontrar el primer numero par");