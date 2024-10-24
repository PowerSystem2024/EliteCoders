package test;

import domain.Persona;

public class Test {
    public static void main(String[] args) {
        final int dni = 42974433;
        // System.out.println("Mi DNI es " + dni);
        System.out.println("Mi atributo constante es " + Persona.PRUEBA_CONSTANTE);

        final Persona persona1 = new Persona();
        // persona1 = new Persona(); No se puede asignar una nueva referencia
        persona1.setNombre("Juan Pérez");
        System.out.println("Persona1 Nombre: " + persona1.getNombre());
        persona1.setNombre("Esteban");
        System.out.println("Persona1 Nombre: " + persona1.getNombre());
    }
}
