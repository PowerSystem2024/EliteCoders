/*
Ejercicio 3:Leer numeros hasta que se introduzca un cero 
Para cada uno indicar si es par o impar
Primero lo haremos con la clase Scanner
Luego con la clase JOPtionPane
||||||||||||AHORA CON SCANNER||||||||||||||
*/
package Ciclos03;

import java.util.Scanner;

public class Ciclos03 {
    
    public static void main(String[] args) {
        //Importo Scanner i declaro variable
        Scanner entrada = new Scanner(System.in);
        
        int num; 
        //Pido al usuario que digite un numero        
        System.out.println("Digite un numero: ");
        num = Integer.parseInt(entrada.nextLine());
        
        //SI es distinto de 0 entra al bucle
        while (num !=0){
            //si es PAR imprimo esto
            if (num %2 ==0){
            
               System.out.println("EL NUMERO ES PAR: "+num); 
               
            }
            //si es IMPAR imprimo esto
            else {
                System.out.println("EL NUMERO ES IMPAR: " +num);
            }
            
            System.out.println("Digite un numero: ");
            num = Integer.parseInt(entrada.nextLine());
        }
        
        //si es igual a 0 imprimo esto
            System.out.println("COLOCO CERO, SALIO DEL PROGRAMA");
        
        
        
    }
    
    
}
