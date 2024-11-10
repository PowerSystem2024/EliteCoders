<template>
  <footer>
    <span>Hecho con ❤️</span>
    <button @click="scrollToTop">Ir arriba</button>
  </footer>
</template>

<script>
export default {
  methods: {
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      })
    }
  }
}
</script>

<style scoped>
footer {
  background-color: var(--color-background-dark);
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
  gap: 5rem;
}
</style>