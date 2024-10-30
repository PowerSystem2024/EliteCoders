import java.util.Scanner;

public class Ejercicio2Ciclos {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int numero;
        do {
            System.out.println("Ingresa un numero: ");
            numero=teclado.nextInt();
            if (numero > 0) {
                System.out.println("El nuemro es positivo");
            } else if (numero < 0) {
                System.out.println("El numero es negativo");
            } 
        } while(numero != 0);
        System.out.println("El programa ha finalizado");
    }
}