/*Proyecto Caja: crear un proyecto segun las especificaciones 
mostradas a continuación.
La formula es: volumen = ancho * alto * profundidad*/
package caja;
public class Caja {

    int alto;
    int ancho;
    int profundidad;

    public int CajaVacio (){
        return alto * ancho * profundidad;
    }

    public int CajaConParametros(int alto, int ancho, int profundidad){
        this.alto = alto;
        this.ancho = ancho;
        this.profundidad = profundidad;
        return this.CajaVacio();
    }
    
}
