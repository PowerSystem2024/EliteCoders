




//Agregar despues de lo de arriva

class Orden{
    static contadorOrdenes=0;
    static getMax_Productos(){//Simula una constante
        return 5;
    }

    constructor(){
        this._idOrden=++Orden.contadorOrdenes;
        this._productos=[];
        this._contadorProductosAgregados=0; 

    }

    get _idOrden(){
        return this._idOrden;
    }

    agregarProducto(producto){
        if(this._productos.lengthz< Orden.getMax_Productos()){
            this._productos.push(producto);
            //this._productos[this._contadorProductosAgregados++]=producto;//segunda sintaxis
        }
        else{
            console.log("No se puedeb agregar mas productos")

        }
    }//fin del metodo agregarProducto

    calcularTottal(){
        let totalVenta= 0;
        for(let producto of this._productos){
            totalVenta+=producto.precio;
        }//fin del ciclo
        return totalVenta;
    }//fin del metodo calcularTotal

    mostrarOrden(){
        let productoOrden=" ";
        for(let producto of this._productos){
            productoOrden +='\n{'+ producto.toString()+" }";
        }//fin del ciclo for
        console.log(`Orden: ${this._idOrden}, Total: $${this.calcularTotal()}, Productos: ${productoOrden}`);

    }// fin metodo mostrarOrder

}//Fin de la clase orden

let producto1=new Producto("Pantalon",200);
let producto2=new Producto("Camisa",150);
let producto3=new Producto("Cinturon",50);
let order1= new Orden();
let order2= new Orden();
order1.agregarProducto(producto1);
order1.agregarProducto(producto2);
order1.agregarProducto(producto3);
order2.agregarProducto(producto1);
order2.agregarProducto(producto2);
order2.agregarProducto(producto3);
order1.mostrarOrden();
order2.mostrarOrden();

console.log(producto1.toString());
console.log(producto2.toString());

