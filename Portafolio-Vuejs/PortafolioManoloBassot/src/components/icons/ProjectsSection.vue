<template>
  <div class="projects-gallery">
    <div class="project-card" v-for="project in projects" :key="project.name">
      <img :src="project.image" alt="Project Image" class="project-image" />
      <h3>{{ project.name }}</h3>
      <p>{{ project.description }}</p>
      <div class="project-buttons">
        <!-- Botón GitHub sin subrayado -->
        <a :href="project.github" target="_blank" class="project-button github-button">
          <i class="fab fa-github icon"></i> GitHub
        </a>

        <!-- Botón de Lenguaje NO cliqueable -->
        <div class="project-button language-button">
          <i :class="project.language.icon" class="icon colored-icon"></i>
          {{ project.language.name }}
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      projects: [
        {
          name: "Inventario PSint",
          description:
            "Sistema de Gestión de Stock: Una solución simple y eficiente para el control de inventario en comercios. Permite visualizar, agregar, modificar y eliminar productos del stock, además de realizar simulaciones de ventas para monitorear la disponibilidad de los productos en tiempo real.",
          image: "/public/logoPseint.png",
          github: "https://github.com/manolobassot",
          language: { name: "PSeint", icon: "fas fa-cogs" }, 
        },
        {
          name: "Inventory Java",
          description:
            "Stock Management System: A simple and efficient inventory control solution for retail businesses. It allows users to view, add, modify, and delete stock items, as well as simulate sales transactions to track product availability in real time.",
          image: "/public/logoJava.png",
          github: "https://github.com/PowerSystem2024/ProyectoEliteCoders",
          language: { name: "Java", icon: "fab fa-java" },
        },
      ],
    };
  },
};
</script>

<style scoped>
/* Contenedor de la galería */
.projects-gallery {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  padding: 20px;
}

/* Tarjeta del proyecto */
.project-card {
  width: 300px;
  background-color: #f4f4f4;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 15px;
}

.project-card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
}

/* Imagen del proyecto */
.project-image {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 8px;
}

/* Botones del proyecto */
.project-buttons {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  margin-top: 10px;
}

/* Estilo general de botones */
.project-button {
  background-color: rgba(0, 123, 255, 0.1);
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  font-size: 1rem;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: background-color 0.3s;
  text-decoration: none; /* Elimina subrayado */
}

/* Hover del botón de GitHub */
.github-button:hover {
  background-color: rgba(0, 123, 255, 0.3);
}

/* Botón de lenguaje NO cliqueable */
.language-button {
  background-color: rgba(0, 123, 255, 0.1);
  cursor: default; /* Cambia el cursor para indicar que no es cliqueable */
}

/* Íconos */
.icon {
  font-size: 1.5rem;
}

/* Mantener colores originales de los íconos */
.colored-icon {
  color: inherit !important;
}
</style>
