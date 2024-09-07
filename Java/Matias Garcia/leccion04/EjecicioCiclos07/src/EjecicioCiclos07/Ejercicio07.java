/*
 Ejercicio 7: Pedir numeros hasta que se introduzca uno negativo
 y calcular la media
||||||||||||||AHORA CON JOPTIONPANE|||||||||||||||||||||||||||||||
*/
package EjecicioCiclos07;


import javax.swing.JOptionPane;
/**
 *
 * @author Matias
 */
public class Ejercicio07 {
    public static void main(String[] args) {
        
        
        //Defino variables
        int suma = 0, num = 0;
        float media = 0;
        int cantidad = 0; // Cambiado a int para contar números
        
        //Creo un bucle dowhile para que entre directamente
        do {            
            //Pido que digite al usuario y lo guardo en num
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            //Para obtener la cantidad de veces que interoduce un numero
            if ( num>1) {
                cantidad++;
            }
            //Sumo el valor de num en suma
            suma=suma+num;
            //luego obtengo el valor de la media dividiendo por la cantidad de numeros ,lo voy a convertir a float
            media=(float)suma/cantidad;
            
            //salgo del bucle por negativo
        } while (num >0);
        //Imprimo la media
         JOptionPane.showMessageDialog(null, "La media incluyendo al número negativo es: " + media);
        
        
        
        
        
        
    }
         
        
        
}

