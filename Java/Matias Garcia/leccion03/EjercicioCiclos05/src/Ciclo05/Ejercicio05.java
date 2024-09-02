/*EJERCICIO 5 :Realizar un juego para adivinar un numero,para
//generar un numero aleatorio entre 0-100. y luego ir pidiendo numeros indicando e "Es mayor" o "Es menor"
//segun sea mayor o menor con respecto a N
EL proceso termina cuando el usuario acierta y mostramos el numero de intentos hechos
||||||||||||||||||||||||||||AHORA CON JOPTIONPANE||||||||||||||||||||||||||||
*/
package Ciclo05;

import javax.swing.JOptionPane;

/**
 *
 * @author Matias
 */
public class Ejercicio05 {
    
    public static void main(String[] args) {
        //DEFINIMOS VARIABLES 
        int aleatorio, conteo =0;
        var numero=0;
        //CREAMOS UN NUMERO ALEATORIO ENTRE 0-100 A ADIVINAR
        aleatorio= (int)(Math.random()*100);
        
        //CREAMOS UN SISTEMA PARA QUE NOS INDIQUE SI TENEMOS QUE DIJITAR UN NUMERO MAYOR O MENOR PARA ENCONTRAR EL NUMERO ALEATORIO ENTRE 0-100 
        do{
            numero =Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")) ;
            
            if(numero < aleatorio){
                
                JOptionPane.showConfirmDialog(null,"Digite un numero mayor: ");
                
            }
            else if(numero > aleatorio){
                JOptionPane.showConfirmDialog(null,"Digite un numero menor: ");
                
            }
            else{
                
                JOptionPane.showConfirmDialog(null,"FELICIDADES!!!!! Has adivinado el numero  ");
                
            }
            //ACTUALIZAMOS LOS INTETOS
            conteo++;
            
            //FIN DEL BUCLE
           }while(numero!= aleatorio);
            
        //IMPRIMIMOS QUE ADIVINO
        
        JOptionPane.showConfirmDialog(null,"\t Adivinastr el numero en: "+conteo+" intentos  ");        
            
        
    }
    
    
    
}
