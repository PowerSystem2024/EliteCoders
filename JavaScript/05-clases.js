//let persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer ya que Persona no esta difinido

class Persona {//Clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    nombreCompleto(){
        return this._nombre + ' ' + this._apellido;
    }
    //Sobreescribiendo el metodo de la clase padre (object)
    toString(){//Regresa un String
        //Se aplica el polimorfismo que significa = miltiples formas en tiempo de ejecicion
        //El metodo que se ejecuta depende se es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }
}

class Empleado extends Persona{//Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }

    //Sobreescritura de metodos
    nombreCompleto(){
        return super.nombreCompleto() + ', ' + this._departamento;
    }
}

let perona1 = new Persona('Martin', 'Perez');
console.log(perona1.nombre)
perona1.nombre = 'Juan Carlos';
console.log(perona1.nombre);
perona1.apellido = 'Gil';
console.log(perona1.apellido);
let perona2 = new Persona('Carlos', 'Lara');
console.log(perona2.nombre)
perona2.nombre = 'Maria Laura';
console.log(perona2.nombre);
perona2.apellido = 'Gimenez';
console.log(perona2.apellido);

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto);

//Object.prototype.toString esta es la manera de acceder a atributos y metodos de manera dinamica
console.log(empleado1.toString());
console.log(perona1.toString());