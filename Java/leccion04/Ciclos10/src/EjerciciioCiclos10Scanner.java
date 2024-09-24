
import java.util.Scanner;

/*
    Ejercicio 10:Pedir 10 numeros y escribir la suma total
hacerlo con la clase scanner y joptionpane
|||||||||||||||||||||||||AHORA CON SCANNER||||||||||||||||||||||||||||
 */

/**
 *
 * @author Matias
 */
public class EjerciciioCiclos10Scanner {
    public static void main(String[] args) {
       Scanner entrada=new Scanner(System.in);
        int num, suma=0;
    
        for(int i=1;i<=10; i++){
            System.out.println("Digita un numero: ");
            num=Integer.parseInt(entrada.nextLine());
            suma+=num;
    
    
    } 
        System.out.println("\nLa suma de todos los numeros es: "+suma);
    }
    
    
}
