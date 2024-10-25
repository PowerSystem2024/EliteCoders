package test;
import ar.com.elitecoders.Utileria;
import static ar.com.elitecoders.Utileria.imprimir;

public class TestUtileria {
    public static void main(String[] args) {
        Utileria.imprimir("Pruebas!");
        imprimir("Probando desde import estático");
        ar.com.elitecoders.Utileria.imprimir("Pruebas llamando directo al paquete y luego a la clase");
    }
}
