<script setup>
import CustomSection from './CustomSection.vue';
import ListItem from './ListItem.vue';

const educationList = [
  {
    anioDesde: '2024',
    anioHasta: 'Actualidad',
    titulo: 'Técnico Universitario en Programación',
    institucion: 'Universidad Tecnológica Nacional'
  },
  {
    anioDesde: '2022',
    anioHasta: '',
    titulo: 'Desarrollo Java',
    institucion: 'Academia Softtek'
  },
  {
    anioDesde: '2021',
    anioHasta: '2022',
    titulo: 'Programador Web Full Stack',
    institucion: 'EGG Education'
  }
]
</script>

<template>
  <CustomSection title="Educación" id="education">
    <div>
      <ul id="education-item-list">
        <li v-for="item in educationList" :key="item.titulo">
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
#profile-photo {
  border-radius: 4px;
}

#education-item-list {
  display: flex;
  flex-direction: column;
  gap: 40px;
}
</style>
