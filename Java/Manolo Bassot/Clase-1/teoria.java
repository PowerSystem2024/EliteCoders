public class teoria {

    public static void main(String[] args) {

        //Ciclo While
        var conteo=0; //Inferencia de tipo
        while (conteo<10) {
            System.out.println("Conteo: "+conteo);
            conteo++;//Aumentamos en 1 la variable
        }    
        //Ciclo do while
        var contador =0;
        do {
            System.out.println("Contador: "+contador);
            contador++;
        } while (contador<10);

        //Ciclo for
            //iterador (i) / condicion  / incremento
        for(var contando=0; contando<10; contando++) {
            System.out.println("Contando: "+contando);
        }

        //Break, continue y etiquetas (labels)
        inicio://Identificador de etiqueta
        for(var contando=0; contando<10; contando++) {
            if (contando % 2 == 0) {
                System.out.println("Contando: "+contando);
                break inicio; //Rompe el ciclo y lo finaliza
            }
        }
        
        inicio2:
        for(var contando=0; contando<10; contando++) {
            if (contando % 2 != 0) {
                continue inicio2; //Le decimos que continue con el siguiente indice
            }
            System.out.println("Contando: "+contando);
        } 
    }
}