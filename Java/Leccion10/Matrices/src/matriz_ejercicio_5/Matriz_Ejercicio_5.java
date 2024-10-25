/*
Ejercicio 5: Crear y cargar una matriz de tamaño n x m, 
mostrar la suma de cada fila y de cada columna.  
*/
package matriz_ejercicio_5;
/**
 * @author matis
 */
import java.util.Scanner;
import javax.swing.JOptionPane;

public class Matriz_Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][], nFilas, nCol;
        
        nFilas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de filas:"));
        nCol = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de columnas:"));
        
        matriz = new int[nFilas][nCol];
        int filas[] = new int[nFilas];
        int columnas[] = new int[nCol];
        
        System.out.println("\nRellenando la Matriz:");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print("Matriz[" + i + "][" + j + "]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
       
        // Mostrar matriz original
        System.out.println("\nMatriz original:");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
        
        // Sumando las filas
        for (int i = 0; i < nFilas; i++) {
            int sumaFilas = 0;
            for (int j = 0; j < nCol; j++) {
                sumaFilas += matriz[i][j];
            }
            filas[i] = sumaFilas;
        } 
        
        // Sumando las columnas
        for (int j = 0; j < nCol; j++) {
            int sumaCol = 0;
            for (int i = 0; i < nFilas; i++) {
                sumaCol += matriz[i][j];
            }
            columnas[j] = sumaCol;
        }
         
        System.out.println("\nLa suma de las filas es: ");
        for (int i = 0; i < nFilas; i++) {
            System.out.println("Fila " + i + ": " + filas[i]);
        }
        
        System.out.println("\nLa suma de las columnas es: ");
        for (int j = 0; j < nCol; j++) {
            System.out.println("Columna " + j + ": " + columnas[j]);
        }
    }
}
