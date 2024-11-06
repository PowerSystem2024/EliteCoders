<template>
  <div class="timeline-container">
    <h2>Studies</h2>
    <div class="timeline">
      <div class="timeline-item" v-for="item in studies" :key="item.title">
        <div class="timeline-content">
          <i :class="item.icon" class="study-icon"></i>
          <h3>{{ item.title }}</h3>
          <p>{{ item.institution }}</p>
          <span>{{ item.period }}</span>
        </div>
      </div>
    </div>

    <h2>Languages and Skills</h2>
    <div class="skills">
      <div class="skill" v-for="skill in skills" :key="skill.name">
        <i :class="skill.icon" class="skill-icon colored-icon"></i>
        <span>{{ skill.name }}</span>
      </div>
    </div>
  </div>
</template>

  
<script>
export default {
  data() {
    return {
      studies: [
        {
          title: "Electrician Technician",
          institution: "Reynaldo Merin School",
          period: "2012 - 2016",
          icon: "fas fa-tools",
        },
        {
          title: "University Technician in Programming",
          institution: "UTN",
          period: "2024 - Present",
          icon: "fas fa-laptop-code",
        },
      ],
      skills: [
        { name: "Java", icon: "fab fa-java" },
        { name: "JavaScript", icon: "fab fa-js" },
        { name: "HTML", icon: "fab fa-html5" },
        { name: "CSS", icon: "fab fa-css3-alt" },
        { name: "Python", icon: "fab fa-python" },
        { name: "MySQL", icon: "fas fa-database" },
        { name: "Vue", icon: "fab fa-vuejs" },
      ],
    };
  },
};
</script>


<style scoped>
/* Contenedor principal */
.timeline-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 20px;
}

/* Título */
h2 {
  font-size: 2rem;
  margin-bottom: 10px;
  color: #007bff;
}

/* Línea de tiempo */
.timeline {
  display: flex;
  overflow-x: auto;
  margin: 20px 0;
  padding: 10px 0;
  scroll-snap-type: x mandatory;
}

/* Item de la línea de tiempo */
.timeline-item {
  flex: 0 0 auto;
  width: 300px; /* Tamaño uniforme */
  margin: 0 15px;
  text-align: center;
  scroll-snap-align: start;
}

.timeline-content {
  background-color: #f4f4f4;
  border-radius: 8px;
  padding: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  height: 300px; /* Asegurar altura uniforme */
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  transition: transform 0.3s;
}

.timeline-content:hover {
  transform: scale(1.05);
}

/* Ícono de estudio */
.study-icon {
  font-size: 3rem;
  color: #007bff;
  margin-bottom: 10px;
}

/* Skills */
.skills {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.skill {
  display: flex;
  align-items: center;
  gap: 10px;
  background-color: #007bff;
  padding: 10px 15px;
  border-radius: 8px;
  transition: background-color 0.3s;
}

.skill:hover {
  background-color: rgba(0, 123, 255, 0.3);
}

/* Íconos con color original */
.skill-icon {
  font-size: 2rem;
}

/* Asegurar que los íconos con colores originales no hereden estilos */
.colored-icon {
  color: inherit !important;
}
</style>
