<script setup>
import CustomSection from './CustomSection.vue'

const skills = [
  { name: "React", icon: "vi-file-type-reactjs" },
  { name: "Java", icon: "vi-file-type-java" },
  { name: "Javascript", icon: "si-javascript" },
  { name: "MySQL", icon: "co-mysql" },
  { name: "SpringBoot", icon: "si-springboot" },
  { name: "Typescript", icon: "vi-file-type-typescript-official" },
]
</script>

<template>
  <CustomSection title="Habilidades/Tecnologías" id="skills">
    <div class="skill-container">
      <ul id="skills-list">
        <li v-for="skill in skills" :key="skill.name" class="skill-item">
          <v-icon :name="skill.icon" scale="2.5" />
          <span>{{ skill.name }}</span>
        </li>
      </ul>
    </div>
  </CustomSection>
</template>

<style scoped>
#skills-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 10px;
  justify-items: center;
}

.skill-item {
  background-color: var(--color-background);
  width: 200px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 10px 20px;
}

@media (max-width: 800px) {
  .skill-item {
    width: 100%;
    gap: 70px;
  }
}

@media (max-width: 600px) {
  .skill-item {
    gap: 20px;
  }
}
</style>
