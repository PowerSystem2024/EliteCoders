package test;

import domain.Persona;

/**
 *
 * @author matis
 */
public class TestMatrices {
    public static void main(String[] args) {
        // Creamos una matriz definiendo las filas y columnas
        int edades[][] = new int[3][2];
        System.out.println("edades= " + edades);
        
        // Llenado manual de la matriz de edades
        edades[0][0] = 5;
        edades[0][1] = 7;
        edades[1][0] = 8; // Es una diferente columna
        edades[1][1] = 4;
        edades[2][0] = 5;
        edades[2][1] = 7;
        
        // Imprimimos los valores de edades
        System.out.println("edades 0-0 = " + edades[0][0]);
        System.out.println("edades 0-1 = " + edades[0][1]);
        System.out.println("edades 1-0 = " + edades[1][0]);
        System.out.println("edades 1-1 = " + edades[1][1]);
        System.out.println("edades 2-0 = " + edades[2][0]);
        System.out.println("edades 2-1 = " + edades[2][1]);
        
        // Recorremos la matriz edades
        System.out.println("\nRecorremos la matriz a través del ciclo for:");
        for (int fila = 0; fila < edades.length; fila++) {
            for (int col = 0; col < edades[fila].length; col++) {
                System.out.println("edades " + fila + "-" + col + ": " + edades[fila][col]);
            }
        }
        
        // Sintaxis simplificada para matriz de frutas
        String frutas[][] = {{"Limón", "Pomelo"}, {"Ciruela", "Kiwi"}, {"Banana", "Pera"}};
        imprimir(frutas);
        
        // Creamos una matriz de objetos de tipo Persona
        Persona personas[][] = new Persona[2][3];
        
        // Asignamos valores a la matriz dentro del rango correcto
        personas[0][0] = new Persona("Matias");
        personas[0][1] = new Persona("Alexander");
        personas[0][2] = new Persona("Franco");
        personas[1][0] = new Persona("Manolo");
        personas[1][1] = new Persona("Marina");
        personas[1][2] = new Persona("Juan");
        
        // Llamamos al método imprimir para mostrar la matriz personas
        imprimir(personas);
    }
    
    // Método genérico para imprimir matrices
    public static void imprimir(Object matriz[][]) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.println("matriz " + i + "-" + j + ": " + matriz[i][j]);
            }
        }
    }
}
