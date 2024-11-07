<script setup>
import img19 from '/src/assets/icons/arg.svg'
import img20 from '/src/assets/icons/eeuu.svg'
import img11 from '/src/assets/icons/git.svg'
import img3 from '/src/assets/icons/html-css.svg'
import img4 from '/src/assets/icons/java.svg'
import img1 from '/src/assets/icons/js.svg'
import img17 from '/src/assets/icons/mysql.svg'
import img2 from '/src/assets/icons/python.svg'
import img5 from '/src/assets/icons/sql.svg'
import img15 from '/src/assets/icons/visual.svg'
import img7 from '/src/assets/icons/vue.svg'

//Se importa ref de vue para poder usarlo
import { ref } from 'vue';
//Se crea un array de objetos con las habilidades
//Este es un array de objetos con habilidades que se pueden modificar o agregar
const habilidades = ref([
  {// Se crea un objeto con id, nombre y habilidades
    id: 1, nombre: 'Lenguajes de Programación', habilidades: [
      //Se crea un objeto con id, nombre, nivel e icono
      { id: 1, nombre: 'JavaScript', icono: img1 },
      { id: 2, nombre: 'Python', icono: img2 },
      { id: 3, nombre: 'HTML/CSS', icono: img3 },
      { id: 4, nombre: 'Java', icono: img4 },
      { id: 5, nombre: 'SQL', icono: img5 }
    ]
  },
  {
    id: 2, nombre: 'Otros', habilidades: [
      { id: 1, nombre: 'Vue.js', icono: img7 },
      { id: 2, nombre: 'Git', icono: img11 },
      { id: 3, nombre: 'Visual Studio Code', icono: img15 },
      { id: 4, nombre: 'MySQL', icono: img17 }
    ]
  },
  {
    id: 5, nombre: 'Idiomas', habilidades: [
      { id: 1, nombre: 'Español', icono: img19 },
      { id: 2, nombre: 'Inglés', icono: img20 }
    ]
  }
])

</script>


<template>
  <!--Este componente vue funciona de esta forma:-->
  <div class="skills-contenedor">
    <!--Se recorre el array habilidades con v-for y se asigna la key habilidad.id-->
    <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
      <!--Se muestra el nombre de la habilidad-->
      <h3>{{ habilidad.nombre }}</h3>
      <ul class="skills">
        <!--Se recorre el array habilidades con v-for y se asigna la key habilidad.id-->
        <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">
          <!--Se muestra el icono de la habilidad y el nombre de la habilidad con su nivel-->
          <img :src="habilidad.icono" :alt="habilidad.nombre">
          <!--Se muestra el icono de la habilidad y el nombre de la habilidad con su nivel-->
          <span>{{ habilidad.nombre }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.skills-contenedor {
  padding: 2rem;
  /*Fondo cargado desde una imagen estatica en Assets*/
  /* background-image: url('/src/assets/fondo-proyectos.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat; */
  /*Fondo con gradiente*/
  background: linear-gradient(-45deg, #062643, #6EACDA, #062643);
}

.skills-categoria {
  margin-bottom: 20px;
}

.skills-categoria h3 {
  display: flex;
  justify-content: left;
  margin-bottom: 10px;
  font-size: 1.5em;
  color: aliceblue;
  font-size: 1.5em;
  font-weight: bold;
}

.skills {
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
  gap: 20px;
}

.skill {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  background-color: rgba(241, 245, 243, 0.856);
  padding: 0.3em;
  border-radius: 8px;
  flex: 1 1 200px;
  max-width: 250px;
}

.skill:hover {
  box-shadow: 0px 0px 8px rgba(255, 255, 255, 0.4);
  cursor: default;
  transition: .4s ease;
}

.skill img {
  width: 35px;
  height: 35px;
}

.skill span {
  font-size: 1em;
  color: #333;
}

@media (max-width: 768px) {
  .skills-categoria h3 {
    justify-content: center;
  }

  .skill {
    justify-content: center;
  }
}
</style>