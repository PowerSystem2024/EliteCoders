/*
 Proyecto caja:
Ejercici 1:Crear un proyecto segun lo especificado
a continuacion.
La formula es:volumen=ancho*alto*profundidad
*/
package proyectocaja;
/**
 *
 * @author Matias
 */
public class ProyectoCaja {

    
    public static void main(String[] args) {
        //Variables localales
        int medidaAncho=3;//Valores ingresados en codigo duro
        int medidaAlto=2;
        int medidaProfundo=6;
        
        Caja caja1=new Caja();//Instanciamos el objeto, contructor vacio
        caja1.ancho=medidaAncho;
        caja1.alto=medidaAlto;
        caja1.profundo=medidaProfundo;
        
        int resultado=caja1.calcularVolumen();//Llamamos al metodo
    
        //Primer resultado
        System.out.println("resultado volumen de caja 1:"+ resultado);
        
        Caja caja2=new  Caja(2,4,6);//Llamamos al constructor 2 con nuevos argumentos;
        //Llamamos con el nuevo objetc al merodo para el nuevo calcuo
        System.out.println("resultado volumen de caja 2: "+caja2.calcularVolumen());
    }   
    
    
    
}
