package domain;

public class Persona {
    public final static int PRUEBA_CONSTANTE = 15;
    private String nombre;

    public void imprimir() {
        System.out.println("Método para imprimir");
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}
