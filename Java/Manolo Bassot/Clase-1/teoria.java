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
        for(var contando=0; contando<10; contando++) {
            System.out.println("Contando: "+contando);
        }
    }
}