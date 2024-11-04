<script setup>
import Marina from '@/assets/FotosIntegrantes/marina.jpeg';
import Franco from '@/assets/FotosIntegrantes/franco.png';
import Manolo from '@/assets/FotosIntegrantes/manolo.jpeg';
import Matias from '@/assets/FotosIntegrantes/matias.jpeg';
import Alexander from '@/assets/FotosIntegrantes/alexander.png';
import { ref } from 'vue';

const integrantes = ref([
  {
    id: 1,
    nombre: 'Marina Evangelista',
    edad: "null",
    localidad: 'Localidad, Buenos Aires',
    foto: Marina,
    github: 'https://github.com/marinaev12',
    instagram: 'Colocar link',
    linkedin: 'Colocar link'
  },
  {
    id: 2,
    nombre: 'Franco Moyano',
    edad: "null",
    localidad: 'San rafael, Mendoza',
    foto: Franco,
    github: 'https://github.com/franmoyano',
    instagram: 'Colocar link',
    linkedin: 'Colocar link'
  },
  {
    id: 3,
    nombre: 'Manolo Bassot',
    edad: 26,
    localidad: 'San rafael, Mendoza',
    foto: Manolo,
    github: 'https://github.com/manolobassot',
    instagram: 'https://www.instagram.com/mbassot/?hl=es',
    linkedin: 'https://www.linkedin.com/in/manolo-bassot-a682531b5'
  },
  {
    id: 4,
    nombre: 'Matias Garcia',
    edad: "null",
    localidad: 'San rafael, Mendoza',
    foto: Matias,
    github: 'https://github.com/hellomaty',
    instagram: 'Colocar link',
    linkedin: 'Colocar link'
  },
  {
    id: 5,
    nombre: 'Alexander Montenegro',
    edad: "null",
    localidad: 'San rafael, Mendoza',
    foto: Alexander,
    github: 'https://github.com/AlexMS7',
    instagram: 'Colocar link',
    linkedin: 'Colocar link'
  },
]);
</script>

<template>
    <div class="timeline">
      <div 
        v-for="(integrante, index) in integrantes" 
        :key="integrante.id" 
        :class="['timeline-item', index % 2 === 0 ? 'left' : 'right']"
      >
        <div class="content">
          <img :src="integrante.foto" :alt="`Foto de ${integrante.nombre}`" class="integrante-foto" />
          <h2>{{ integrante.nombre }}</h2>
          <p>Edad: {{ integrante.edad }}</p>
          <p>Localidad: {{ integrante.localidad }}</p>
          <div class="redes">
            <a :href="integrante.github" target="_blank"><i class="fab fa-github"></i></a> | 
            <a :href="integrante.instagram" target="_blank"><i class="fab fa-instagram"></i></a> | 
            <a :href="integrante.linkedin" target="_blank"><i class="fab fa-linkedin"></i></a>
          </div>
        </div>
      </div>
    </div>
  </template>

<style scoped>
/* Contenedor general de la línea de tiempo */
.timeline {
  position: relative;
  width: 100%;
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
}

/* Línea central */
.timeline::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 0;
  width: 4px;
  height: 100%;
  background-color: #0277bd; /* Azul oscuro */
  transform: translateX(-50%);
}

/* Elemento de la línea de tiempo */
.timeline-item {
  position: relative;
  width: 45%;
  margin-bottom: 30px;
}

/* Alineación a la izquierda y derecha */
.timeline-item.left {
  left: 0;
  text-align: right;
}

.timeline-item.right {
  left: 55%;
}

/* Contenido del integrante */
.content {
  background-color: #202020; /* Celeste claro */
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  position: relative;
}

.content::after {
  content: "";
  position: absolute;
  top: 15px;
  width: 15px;
  height: 15px;
  background-color: #0277bd;
  border-radius: 50%;
}

.timeline-item.left .content::after {
  right: -7px;
}

.timeline-item.right .content::after {
  left: -7px;
}

/* Foto del integrante */
.integrante-foto {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}



/* Responsividad */
@media (max-width: 768px) {
  .timeline-item {
    width: 100%;
    left: 0;
    text-align: center;
  }

  .timeline-item.right {
    left: 0;
  }

  .content::after {
    display: none;
  }
}
.redes {
  display: flex;
  justify-content: center; /* Centra los íconos */
  gap: 10px; /* Espacio entre los íconos */
}
.redes i {
  font-size: 24px; /* Tamaño del ícono */
  color: #333; /* Color del ícono */
}
</style>