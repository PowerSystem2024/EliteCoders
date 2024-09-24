
import javax.swing.JOptionPane;




/*
    Ejercicio 10:Pedir 10 numeros y escribir la suma total
hacerlo con la clase scanner y joptionpane
|||||||||||||||||||||||||AHORA CON JOpionPANE||||||||||||||||||||||||||||
 */

/**
 *
 * @author Matias
 */
public class EjercicioCiclos10JOptionPane {
    public static void main(String[] args) {
       
        int num, suma=0;
    
        for(int i=1;i<=10; i++){
            num=Integer.parseInt(JOptionPane.showInputDialog("Digite el numero: "));
            suma+=num;
    
    
    } 
        
        JOptionPane.showMessageDialog(null, "La suma de rodos los numeros es: "+suma);
    }
}
