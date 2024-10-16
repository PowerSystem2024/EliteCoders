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
        return this.nombre+' '+this.apellido;
    }

    //Sobreescribiendo el metodo de la clase padre(Obect)

    toString(){ //Regresa un String
        //se aplica el polimorfismo = multiples formas en tiempo de ejecucion
        //El metodo que se eecuta depende si es una referencia de tipo padre o hija
        return this.nombreCompleto(); 
    }

    static saludar(){
        console.log('Saludos desde este método static');
    }

    static saludar2(persona){
        console.log(persona.nombre);
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

    //Sobreescritura

    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento;
    }

}

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre)
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
persona1.apellido = 'Gil';
console.log(persona1.apellido);
let perona2 = new Persona('Carlos', 'Lara');
console.log(perona2.nombre)
perona2.nombre = 'Maria Laura';
console.log(perona2.nombre);
perona2.apellido = 'Gimenez';
console.log(perona2.apellido);

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

// Object.prototype.toString manera de acceder a atributos y metodos de manera dinamica
console.log(empleado1.toString())
console.log(persona1.toString());

// persona1.saludar(); No se utiliza desde el objeto
Persona.saludar();
Persona.saludar2(persona1);