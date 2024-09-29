/*
Ejercicio 2: Leer un numero e indicar si es positivo o negativo.
El proceso se repetira hasta que se ponga un cero 0
*/
package Ciclos01;

import  java.util.Scanner;
/**
 *
 * @author Matias
 */
public class Ejercicio02 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num;
       
        System.out.println("Digite un numero: ");
        num = Integer.parseInt(entrada.nextLine());
        
        while (num != 0 ){
            
            System.out.println("El numero es "+ num+ " por tanto sigue");
            System.out.println("Digite otro numero: ");
            num=Integer.parseInt(entrada.nextLine());
       
        }
        System.out.println("El programa a finalizado por el numero 0");    
        }
        
        
     
        
        
        
        
    }
     
   
    
    
    
    
    
    
}
