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
import imagenPseint from '/public/logoPseint.png';
import imagenJava from '/public/logoJava.png';
import imagenAntivirus from '/public/antivirus.png'
export default {
  data() {
    return {
      projects: [
        {
          name: "Inventory PSint",
          description:
            "Inventory Management System: A simple and efficient solution for managing in-store inventory. It allows you to visualize, add, modify and remove products from stock, as well as run sales simulations to monitor product availability in real time.",
          image: imagenPseint,
          github: "https://github.com/AlexMS7?tab=repositories",
          language: { name: "PSeint", icon: "fas fa-cogs" },
        },
        {
          name: "Inventory Java",
          description:
            "Stock Management System: A simple and efficient inventory control solution for retail businesses. It allows users to view, add, modify, and delete stock items, as well as simulate sales transactions to track product availability in real time.",
          image: imagenJava,
          github: "https://github.com/PowerSystem2024/ProyectoEliteCoders",
          language: { name: "Java", icon: "fab fa-java" },
        },
        {
          name: "Antivirus",
          description:
            "Provides essential protection against malware and viruses. Users can scan, detect, and remove threats, ensuring safer browsing. Ideal for those seeking a simple, effective security solution.",
          image: imagenAntivirus,
          github: "https://github.com/AlexMS7?tab=repositories",
          language: { name: "Antivirus", icon: "fab fa-Logoantivirus" }
        },
      ],
    };
  },
};
</script>

<style scoped>

.projects-gallery {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  padding: 20px;
}


.project-card {
  width: 300px;
  background-color: #f4f4f4;
  color: #4B0082;
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


.project-image {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 8px;
}


.project-buttons {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  margin-top: 10px;
}


.project-button {
  background-color: rgba(75, 0, 130, 0.1);
  color: #4B0082;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  font-size: 1rem;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: background-color 0.3s, box-shadow 0.3s;
  text-decoration: none;
}

.project-button:hover {
  background-color: rgba(75, 0, 130, 0.3);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}


.github-button:hover {
  background-color: rgba(75, 0, 130, 0.3);
}


.language-button {
  background-color: rgba(75, 0, 130, 0.1);
  cursor: default;
}

.icon {
  font-size: 1.5rem;
}


.colored-icon {
  color: inherit !important;
}
</style>
