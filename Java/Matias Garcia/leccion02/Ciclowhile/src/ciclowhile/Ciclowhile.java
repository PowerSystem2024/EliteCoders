/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ciclowhile;

import javax.print.DocFlavor;

/**
 *
 * @author Matias
 */
public class Ciclowhile {

    /**
     * @param args the command line arguments
     */
    //Ciclo WHILE
    public static void main(String[] args) {
        var conteo =0;
        while (conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo++;
        
        
        }
    //Ciclo DO WHILE
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
  
        }while (contador <=7 );           
            
    //ciclo FOR y la palabra break y 
        
        for (var contando= 0; contando < 7; contando++){
            
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break;
            }
        
        }
        //Palabra continue
        for (var contando= 0; contando < 7; contando++){
            
            if(contando % 2 != 0){
                
                continue;//vuelve al principio del ciclo
                
            }
            System.out.println("contando = " + contando);
        }
        
        
        //Etiquetas Labels
        inicio:
        for (var contando= 0; contando < 7; contando++){
            
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break inicio;
            }
        
        }
        
        
        
    }
    
}
