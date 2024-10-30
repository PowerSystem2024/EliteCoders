package test;

import domain.Persona;

/**
 * @author matis
 */
public class TestArreglosObjetc {
    public static void main(String[] args) {
        //Creamos el arreglo
        Persona personas[]=new  Persona[2];
        
        //asignamos valores al arreglo y imprimimos
        personas[0]=new Persona("Matias");
        personas[1]=new Persona("Garcia");
        System.out.println("personas 0 =" + personas[0]);
        System.out.println("personas 1 =" + personas[1]);
        
        // Recorremos el arreglo y imprimimos
        for(int i =0; i < personas.length; i ++){
            System.out.println("personas"+i+" = "+personas[i]);
        }
        
    //trabajando con arreglos sintxis resumida
        String frutas[]={"Banana","Pera","Durasno"};
        
        //recorremos el arreglo frutas
        for (int i = 0; i < frutas.length; i++) {
            System.out.println("frutas= "+frutas[i]);
        }
    }
}
