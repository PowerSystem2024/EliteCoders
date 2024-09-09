import javax.swing.JOptionPane;

public class Ejercicio2JOptionPane {

    public static void main(String[] args) {
        int numero;
    do {
        
            numero=Integer.parseInt(JOptionPane.showInputDialog("Ingresa un numero: "));
            if (numero > 0) {
                System.out.println("El nuemro es positivo");
            } else if (numero < 0) {
                System.out.println("El numero es negativo");
            } 
        } while(numero != 0);
        System.out.println("El programa ha finalizado");
    }
}
