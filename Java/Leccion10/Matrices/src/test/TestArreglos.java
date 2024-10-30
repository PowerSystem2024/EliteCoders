package test;
/**
 * @author matis
 */
public class TestArreglos {
    public static void main(String[] args) {
        //Creacion de un arreglo y imprimimos
        int edades []= new int[3];
        System.out.println("edades= "+edades);
        
        //Modificamos el arreglo y imprimimos
        edades[0]=17;
        System.out.println("edades 0= "+ edades[0]);
        
        //Modificamos el arreglo y imprimimos
        edades[1]=20;
        System.out.println("edades 1= "+ edades[1]);
        
        //Modificamos el arreglo y imprimimos
        edades[2]=40;
        System.out.println("edades 2= "+ edades[2]);
        
        //esto es un error 
        //edades[3] = 7;
        
        //Iteramos los elementos del arrai
        for(int i=0; i < edades.length; i++){
            System.out.println("Edades y sus elementos "+i+":"+ edades[i]);
        }
    }
}
