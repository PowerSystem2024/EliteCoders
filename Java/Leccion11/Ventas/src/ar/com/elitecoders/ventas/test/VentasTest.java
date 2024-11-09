package ar.com.elitecoders.ventas.test;

import ar.com.elitecoders.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 950);
        Producto producto2 = new Producto("Camisa", 450);
        Producto producto3 = new Producto("Zapato", 150);
        Producto producto4 = new Producto("Hoodie", 550);
        Producto producto5 = new Producto("Medias", 50);
        Producto producto6 = new Producto("Cinturon", 90);
        Producto producto7 = new Producto("Boxe", 20);
        Producto producto8 = new Producto("Saco", 350);
        Producto producto9 = new Producto("Gabardina", 1050);
        Producto producto10 = new Producto("Corbata", 44);

        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto5);
        orden1.agregarProducto(producto6);
        orden1.agregarProducto(producto7);
        orden1.mostrarOrden();

        //Orden tarea

        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto8);
        orden2.agregarProducto(producto9);
        orden2.agregarProducto(producto10);
        orden2.mostrarOrden();
    }
}
