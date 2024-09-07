/*
EJercicio 4: Pedir numeros hasta que se teclee uno negativo, y mostrar
cuantos numeros se han introducidos.
Lo hacemmos primero con la clese scanner 
luego lo hacemos con la clase JOptionPane
|||||||||||AHORA CON SCANNER|||||||||||||||
*/  
package Ciclos04;

import java.util.Scanner;
/**
 *
 * @author Matias
 */
public class Ciclos04 {
    public static void main(String[] args) {
        
        //Importo Scanner i declaro variables
        Scanner entrada = new Scanner(System.in);
        
        int num;
        int cantida_num=0;
        
        //Pido al usuario que digite un numero        
        System.out.println("Digite un numero: ");
        num = Integer.parseInt(entrada.nextLine());
        
        //SI es distinto de NEGATIVO entra al bucle
        while (num >=0){
            //INCREMENTO CANTIDA_NUM PARA QUE SE MUESTRE EN EL INTENTO
            cantida_num++;
                    
            //imprimo LA CANTIDAD DE NUMEROS INTRODUCIDOS
            System.out.println("La cantidad de numeros introducidos: "+cantida_num); 
            
            //LE PEDIMOS AL USUARIO QUE DIGITE OTRO NUMERO
            System.out.println("Digite otro numero numero: ");
            num = Integer.parseInt(entrada.nextLine());
        }
        
        //si es NEGATIVO imprimo esto
         System.out.println("COLOCO UN NUMERO NEGATIVO, SALIO DEL PROGRAMA");
        
        
        
    }
}
