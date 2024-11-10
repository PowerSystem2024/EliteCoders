<template>
  <div class="container">
    <span id="anio">{{ anioDesde }} <span v-if="anioHasta">{{ `- ${anioHasta}` }}</span></span>
    <div id="education-item">
      <span>{{ titulo }} - {{ institucion }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "ListItem",
  props: {
    anioDesde: {
      type: String,
      required: true
    },
    anioHasta: {
      type: String,
      required: false
    },
    titulo: {
      type: String,
      required: true
    },
    institucion: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
#anio {
  width: 150px;
  max-width: 150px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: 14px;
}

.container {
  font-size: 18px;
  display: flex;
  flex-direction: column;
}

/* #education-item {
  
} */
</style>