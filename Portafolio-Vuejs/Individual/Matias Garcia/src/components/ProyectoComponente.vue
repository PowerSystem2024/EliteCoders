<script setup>
import proyecto1 from '/src/assets/videojuego.svg';
import proyecto2 from '/src/assets/db.svg';
import proyecto3 from '/src/assets/nasa.svg';
import proyecto4 from '/src/assets/petroleo.svg';


import { ref } from 'vue';

var Proyectos = ref([]);

Proyectos.value = ([
  {
    id: 1,
    src: proyecto1,
    titulo: "Game Horror",
    descripcion: "Desarrolle un videojuego en unity de terror, ideal para jugar en el tiempo libre y sumergirse en una experiencia unica .",
    projectoLink: "https://github.com/matiasgarcia-dot",
    githubLink: "https://github.com/matiasgarcia-dot"
  },
  {
    id: 2,
    src: proyecto2,
    titulo: "Trabajo en Base de Datos",
    descripcion: "Desarrolle una base de datos para una empresa de mercaderia.Esta permite un mejor control de sus alimentos, la fecha de ingreso, el vencimiento, la demanda y demas.",
    projectoLink: "https://github.com/matiasgarcia-dot",
    githubLink: "https://github.com/matiasgarcia-dot"
  },
  {
    id: 3,
    src: proyecto3,
    titulo: "Detector de Estrellas",
    descripcion: "Cree un sotware a medida para la Nasa. Este permite que los telescopios de alta precicion, puedan detectar fenomenos y anomalias del espacio .",
    projectoLink: "https://github.com/matiasgarcia-dot",
    githubLink: "https://github.com/matiasgarcia-dot"
  },
  {
    id: 4,
    src: proyecto4,
    titulo: "Trabaje para YPF en Gestion de Riesgos",
    descripcion: "Segun los datos que me proporcionaban las diferentes bases de datos, cree un sotware que estima cuando se debe reacondicionar la estacion.Esto con el objetivo, de evitar derrame de petroleo en el mar",
    projectoLink: "https://github.com/matiasgarcia-dot",
    githubLink: "https://github.com/matiasgarcia-dot"
  },
])

</script>

<template>
  <!-- Aquí va el código HTML de la galería de proyectos -->
  <div class="galeria">

    <li class="proyecto" v-for="proyecto in Proyectos" :key="proyecto.id">
      <!-- Muestra la imagen del proyecto utilizando : que es una directiva de enlace de atributo en Vue.js -->
      <img :src="proyecto.src" :alt="proyecto.titulo">
      <div class="proyecto-info">

        <h3>{{ proyecto.titulo }}</h3>
        <p>{{ proyecto.descripcion }}</p>
        <div class="proyecto-links">
          <a :href="proyecto.projectoLink" class="btn-ver-mas" target="_blank" rel="noopener noreferrer">Ver
            Proyecto</a>
          <a :href="proyecto.githubLink" class="github-link" target="_blank" rel="noopener noreferrer">Ver
            codigo en GitHub </a>
        </div>
      </div>
    </li>
  </div>
</template>

<style scoped>
/* Estilos Fondo Animado de Css de la galería */
/* La clase 'galeria' es el contenedor principal de la galería de proyectos */
.galeria {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;
  justify-content: center;
  background: linear-gradient(-45deg, #1f0226, #6e0359, #6EACDA, #e2b6d5);
  background-size: 400% 400%;
  animation: gradient 15s ease infinite;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

.proyecto {
  display: flex;
  flex-direction: column;
  border: 2px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  background-color: #f9f9f9;
  max-width: 222px;
  flex: 1 1 300px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.proyecto:hover {
  transform: scale(1.01);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.proyecto img {
  width: 100%;
  height: auto;
  display: block;
}

.proyecto-info {
  padding: 15px;
  text-align: center;
}

.proyecto-info h3 {
  margin: 10px 0;
  font-size: 1.3em;
  color: #333;
}

.proyecto-info p {
  margin: 10px 0;
  font-size: 1em;
  color: #666;
}

.proyecto-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 30px;
}

.proyecto-links .btn-ver-mas {
  background-color: #007BFF;
  color: #fff;
  padding: 10px 15px;
  border-radius: 5px;
  text-decoration: none;
  transition: background-color 0.3s;
  margin-top: 1rem;
}

.proyecto-links .btn-ver-mas:hover {
  background-color: #0056b3;
}

.proyecto-links .github-link {
  color: #333;
  text-decoration: none;
  font-size: 0.9em;
}

.proyecto-links .github-link:hover {
  text-decoration: underline;
}
</style>