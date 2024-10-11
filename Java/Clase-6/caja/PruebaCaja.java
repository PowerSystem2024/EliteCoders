package caja;
public class PruebaCaja {

    public static void main(String[] args) {
        Caja caja1 = new Caja();
        caja1.alto = 10;
        caja1.ancho = 5;
        caja1.profundidad = 2;
        System.out.println("El volumen de la caja 1 es: " + caja1.CajaVacio());

        Caja caja2 = new Caja();
        caja2.CajaConParametros(20, 10, 5);
        System.out.println("El volumen de la caja 2 es: " + caja2.CajaVacio());
    }
}
