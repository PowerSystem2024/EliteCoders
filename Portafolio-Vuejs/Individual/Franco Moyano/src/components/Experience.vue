<script setup>
import CustomSection from './CustomSection.vue';
import ListItem from './ListItem.vue';

const experienceList = [
  {
    anioDesde: '2022',
    anioHasta: 'Actualidad',
    titulo: 'Desarrollador Fullstack React - Java',
    institucion: 'Softtek'
  }
]
</script>

<template>
  <CustomSection title="Experiencia" id="experience">
    <div>
      <ul id="experience-item-list">
        <li v-for="item in experienceList" :key="item.titulo">
          <ListItem
            :anioDesde="item.anioDesde"
            :anioHasta="item.anioHasta"
            :titulo="item.titulo"
            :institucion="item.institucion"
          />
        </li>
      </ul>
    </div>
  </CustomSection>
</template>

<style scoped>

#experience-item-list {
  display: flex;
  flex-direction: column;
  gap: 40px;
}
</style>
