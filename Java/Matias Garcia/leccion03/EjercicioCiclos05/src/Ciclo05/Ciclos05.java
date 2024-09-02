/*EJERCICIO 5 :Realizar un juego para adivinar un numero,para
//generar un numero aleatorio entre 0-100. y luego ir pidiendo numeros indicando e "Es mayor" o "Es menor"
//segun sea mayor o menor con respecto a N
EL proceso termina cuando el usuario acierta y mostramos el numero de intentos hechos
||||||||||||||||||||AHORA CON LA CLASE SCANNER||||||||||||||||||||||||||||||
*/
package Ciclo05;

import java.util.Scanner;

/**
 *
 * @author Matias
 */
public class Ciclos05 {
    public static void main(String[] args) {
        //DEFINIMOS VARIABLES Y LLAMAMMOS A SCANNER
        Scanner entrada = new  Scanner(System.in);
        int numero, aleatorio, conteo =0;
        
        //CREAMOS UN NUMERO ALEATORIO ENTRE 0-100 A ADIVINAR
        aleatorio= (int)(Math.random()*100);
        
        //CREAMOS UN SISTEMA PARA QUE NOS INDIQUE SI TENEMOS QUE DIJITAR UN NUMERO MAYOR O MENOR PARA ENCONTRAR EL NUMERO ALEATORIO ENTRE 0-100 
        do{
            System.out.println("Digite un numero: ");
            numero= Integer.parseInt(entrada.nextLine());
            
            if(numero < aleatorio){
                System.out.println("Digite un numero mayor: ");
                
            }
            else if(numero > aleatorio){
                System.out.println("Digite un numero menor: ");
                
            }
            else{
                System.out.println("FELICIDADES!!!!! Has adivinado el numero ");
                
            }
            //ACTUALIZAMOS LOS INTETOS
            conteo++;
            
            //FIN DEL BUCLE
           }while(numero!= aleatorio);
            
        //IMPRIMIMOS QUE ADIVIONP
        System.out.println("\t Adivinastr el numero en: "+conteo+" intentos");
                
            
        
    }
}
