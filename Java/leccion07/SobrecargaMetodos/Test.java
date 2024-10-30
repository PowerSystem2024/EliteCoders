public class Test {
    public static void main(String[] args) {
        var resultado1 = Operaciones.sumar(1, 2);
        System.out.println(resultado1);

        var resultado2 = Operaciones.sumar(5.0, 1.5);
        System.out.println(resultado2);

        var resultado3 = Operaciones.sumar(2, 4L);
        System.out.println(resultado3);
    }
}
