/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Matias
 */
public class PasoPorValor {
    public static void main(String[] args) {
        var valorX=20;
        System.out.println("valorX="+valorX);
        cambioValor(valorX);//Solo le enviamos una copia
        System.out.println("valorX="+valorX);
        
    }
    
    public  static void cambioValor(int arg1){
        System.out.println("Arg1= "+arg1);
        arg1=15;
                
    }
}
