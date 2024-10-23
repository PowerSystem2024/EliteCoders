/* Ejercicio 5: Realizar un juego para adivinar un numero,
para ello generar un numero aleatorio entre 0-100, y
luego ir pidiendo numeros indicando si es mayor o menor.
El proceso termina cuando el usuario acierta y mostramos
el numero de intentos.
 */

import javax.swing.JOptionPane;
 public class Ejercicio5CiclosJOption {
     public static void main(String[] args) {
         int numero = (int) (Math.random() * 100);
         int intentos = 0; 
         int num = 0;
 
         while (numero != num) {
             num = Integer.parseInt(JOptionPane.showInputDialog("Ingresa un numero: "));
             intentos++;
             if (num > numero) {
                 JOptionPane.showMessageDialog(null, "El numero es menor\n");
             } else if (num < numero) {
                 JOptionPane.showMessageDialog(null, "El numero es mayor\n");
             } else {
                 JOptionPane.showMessageDialog(null, "Felicidades, adivinaste el numero en " + intentos + " intentos");
             }
         }
     }
     
 }
 