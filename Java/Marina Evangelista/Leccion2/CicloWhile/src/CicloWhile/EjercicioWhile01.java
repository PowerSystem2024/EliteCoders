
package CicloWhile;

public class EjercicioWhile01 {
    
    public static void main(String[] args) {
        var conteo = 0; //inferencia de tipos
        while (conteo <= 7){
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable
            
        }
        
        //Ciclo DoWhile
        var contador = 0;
        do{
            System.out.println("contador = " + contador); 
            contador++;
        }while(contador <7) ;    

    //Ciclo For - p num determinado de iteraciones
    /**
     * 1-variable, 2-condicion a cumplir, 3-iteraccion como será
     */
    Inicio:
    for (var contando = 0; contando < 7; contando++){
        if (contando % 2 == 0){
            System.out.println("contando = " + contando);
            break Inicio; //para en el primer que /2 es 
        }
    }
    
    // Etiquetas - se combinan con continue or break
    for (var contando = 0; contando < 7; contando++){
        if (contando % 2 == 0){
            System.out.println("contando = " + contando);
}           
}
}
}
