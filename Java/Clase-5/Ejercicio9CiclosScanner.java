/* Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar si la fecha es correcta.
Suponiendo que todos los meses son de 30 dias.
 */

import java.util.Scanner;

public class Ejercicio9CiclosScanner {
    public static void main(String[] args) {
        Scanner valor = new Scanner(System.in);
        System.out.println("Ingresa el dia: ");
        int dia = valor.nextInt();
        System.out.println("Ingresa el mes: ");
        int mes = valor.nextInt();
        System.out.println("Ingresa el año: ");
        int año = valor.nextInt();

        if (dia > 0 && dia < 31 && mes > 0 && mes < 13 && año > 0 && año < 2025) {
            System.out.println("La fecha es correcta");
            System.out.println("El dia es " + dia + " del mes " + mes + " del año " + año);
        } else {
            System.out.println("La fecha es incorrecta");
        }
        valor.close();
    }
}