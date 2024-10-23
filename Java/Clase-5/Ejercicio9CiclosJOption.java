/* Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar si la fecha es correcta.
Suponiendo que todos los meses son de 30 dias.
 */
import javax.swing.JOptionPane;
 public class Ejercicio9CiclosJOption {
     public static void main(String[] args) {
      
         
         int dia = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el dia: "));
         int mes = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el mes: "));
         int año = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el año: "));
 
         if (dia > 0 && dia < 31 && mes > 0 && mes < 13 && año > 0 && año < 2025) {
             JOptionPane.showMessageDialog(null, "La fecha es correcta");
             JOptionPane.showMessageDialog(null, "El dia es " + dia + " del mes " + mes + " del año " + año);
         } else {
             JOptionPane.showMessageDialog(null, "La fecha es incorrecta");
         }
     }
 }