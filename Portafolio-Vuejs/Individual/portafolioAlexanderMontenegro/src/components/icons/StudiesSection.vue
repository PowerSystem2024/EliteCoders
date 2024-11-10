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
          title: "Networks & Telecommunications",
          institution: "Formaciones Cisco Networking",
          period: "2024 - Present",
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

.timeline-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 20px;
}


h2 {
  font-size: 2rem;
  margin-bottom: 10px;
  color: #6A0DAD;
}


.timeline {
  display: flex;
  overflow-x: auto;
  margin: 20px 0;
  padding: 10px 0;
  scroll-snap-type: x mandatory;
}


.timeline-item {
  flex: 0 0 auto;
  width: 300px;
  margin: 0 15px;
  text-align: center;
  scroll-snap-align: start;
}

.timeline-content {
  background-color: #1E1E1E;
  color: #6A0DAD;
  border-radius: 8px;
  padding: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  transition: transform 0.3s, box-shadow 0.3s;
}

.timeline-content:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 15px rgba(106, 13, 173, 0.5);
}


.study-icon {
  font-size: 3rem;
  color: #6A0DAD;
  margin-bottom: 10px;
}


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
  background-color: rgba(106, 13, 173, 0.2);
  color: #FFFFFF;
  padding: 10px 20px;
  border-radius: 8px;
  font-weight: bold;
  transition: background-color 0.3s, box-shadow 0.3s;
}

.skill:hover {
  background-color: #6A0DAD;
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.3);
  color: #FFFFFF;
}


.skill-icon {
  font-size: 2rem;
  color: #FFFFFF;
}


.colored-icon {
  color: inherit !important;
}
</style>
