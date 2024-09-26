/*
Ejercicio 6: Pedir nu,eros hasta que se teclee un 0,
mostrar la suma de todos los numeros introducisos
*/

import java.util.Scanner;

public class Ciclos06 {
    public static void main(String[] args) {
        //Llamo a la clase sxanner
        Scanner entrada = new Scanner(System.in);
        //defino variables
        int num,suma = 0;
        
        //Que entre directamente al ciclo
        do {            
            //Pido al usuario que digite un numero        
            System.out.println("Digite un numero: ");
            //Convierto el valor a entero
            num = Integer.parseInt(entrada.nextLine());
            //Sumo la variable num y la guardo en suma
            suma+=num;
            //Imprimo la suma
            System.out.println("La suma de los numeros son: "+suma);
            //Fin del ciclo
        } while (num!=0);
        //Imprimo la suma
        System.out.println("La suma de los numeros son: "+suma);
    }
    
    
}
