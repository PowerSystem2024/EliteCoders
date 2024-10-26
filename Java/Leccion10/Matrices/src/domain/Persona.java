package domain;
/**
 * @author matis
 */
public class Persona {
    private  String nombre;
    
    //Creamos el contructor
    public Persona(String nombre) {
        this.nombre = nombre;
    }
    
    //Creamos el getter y el setter
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    //Creamos el tostring
    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + '}'+", "+super.toString();
    }
    
    
}
