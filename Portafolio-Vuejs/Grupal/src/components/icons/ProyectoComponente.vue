<script setup>
import proyecto1 from '/src/assets/antivirus.svg';
import proyecto2 from '/src/assets/db.svg';
import proyecto3 from '/src/assets/mantenimiento.svg';
import proyecto4 from '/src/assets/api.svg';


import { ref } from 'vue';

var Proyectos = ref([]);

Proyectos.value = ([
    {
        id: 1,
        src: proyecto1,
        titulo: "Antivirus",
        descripcion: "Desarrollamos un antivirus que detecta y elimina amenazas en tiempo real, con una interfaz intuitiva y funciones avanzadas como protección en la nube y actualizaciones automáticas.",
        projectoLink: "https://www.google.com.ar",
        githubLink: "https://github.com/usuario/proyecto"
    },
    {
        id: 2,
        src: proyecto2,
        titulo: "Trabajo en Base de Datos",
        descripcion: "Desarrollamos un sistema para optimizar la gestión de inventarios y mejorar la experiencia del cliente en una empresa de comercio electrónico, utilizando tecnologías avanzadas y algoritmos de predicción.",
        projectoLink: "https://www.google.com.ar",
        githubLink: "https://github.com/usuario/proyecto"
    },
    {
        id: 3,
        src: proyecto3,
        titulo: "Mantenimiento sobre el software de Gestion de Inventario",
        descripcion: "Después de implementar el sistema de gestión de inventarios, el equipo de programadores ofreció soporte continuo, actualizaciones periódicas y capacitación al personal, asegurando un sistema optimizado y confiable que contribuyó al éxito del negocio.",
        projectoLink: "https://www.google.com.ar",
        githubLink: "https://github.com/usuario/proyecto"
    },
    {
        id: 4,
        src: proyecto4,
        titulo: "Api para servicios financieros",
        descripcion: "Se desarrollo una API segura y escalable para una empresa de servicios financieros, mejorando la integración de aplicaciones y el acceso a datos financieros.",
        projectoLink: "https://www.google.com.ar",
        githubLink: "https://github.com/usuario/proyecto"
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
                    <a :href="proyecto.githubLink" class="github-link" target="_blank" rel="noopener noreferrer">Ver codigo en GitHub </a>
                </div>
            </div>
        </li>
    </div>
</template>

<style scoped>
/* .galeria{
      width: 100%;
      height: 100vh;
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: center;
      background-image: url('/src\assets\fondoProyectos.jpg');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
} */

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
    background: linear-gradient(-45deg, #021526, #03346E, #6EACDA, #E2E2B6);
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
    transform: scale(1.05);
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