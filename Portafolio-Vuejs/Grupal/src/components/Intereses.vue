<script setup>
import { ref } from 'vue';
import FondoLava from './FondoLava.vue';
//Este es un arreglo con ref para que se pueda reactivar el cambio de los intereses
const intereses = ref([
  'Desarrollo web',
  'Desarrollo mobile',
  'Inteligencia Artificial'
])
</script>

<template>
  <div class="intereses-contenedor">
    <FondoLava />
    <ul class="contenedor-lista">
      <li class="item" v-for="interes in intereses" :key="interes">
        {{ interes }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.intereses-contenedor {
  display: flex;
  position: relative;
  margin: 0 auto;
  max-width: 100%;
  padding: 1rem;
}

.contenedor-lista {
  list-style-type: none;
  padding: 1rem;
  margin-bottom: .5rem;
  color: var(--vt-c-white-soft);
  font-size: 1.4rem;
}

.item {
  margin-bottom: 1rem;
  color: #FFF;
}
</style>