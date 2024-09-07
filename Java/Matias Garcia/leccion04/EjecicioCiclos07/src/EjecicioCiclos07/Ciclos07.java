/*
 Ejercicio 7: Pedir numeros hasta que se introduzca uno negativo
 y calcular la media
||||||||||||||AHORA CON SCANNER|||||||||||||||||||||||||||||||
*/
package EjecicioCiclos07;
import java.util.Scanner;
/**
 *
 * @author Matias
 */
public class Ciclos07 {
    public static void main(String[] args)  {
        //Llamo a scanner
        Scanner entreada = new Scanner(System.in);
        //Defino variables
        float num,suma=0;
        float media,cantidad=0;
        //Creo un bucle dowhile para que entre directamente
        do {            
            //Pido que digite al usuario y lo guardo en num
            System.out.println("Digite un numero: ");
            num=Integer.parseInt(entreada.nextLine());
            //Para obtener la cantidad de veces que interoduce un numero
            if ( num>1) {
                cantidad++;
            }
            //Sumo el valor de num en suma
            suma=suma+num;
            //luego obtengo el valor de la media dividiendo por la cantidad de numeros
            media=suma/cantidad;
            
            //salgo del bucle por negativo
        } while (num >0);
        //Imprimo la media
        System.out.println("La media incluyendo al numero negativo es: "+media);
        
        
        
        
    }
    
}
        
        
    
    

