<script setup>
const items = [
  { name: "Inicio", link: "#presentation" },
  { name: "Educación", link: "#education" },
  { name: "Experiencia", link: "#experience" },
  { name: "Habilidades/Tecnologías", link: "#skills" }
]
</script>

<template>
  <nav class="nav">
    <ul class="list">
      <li class="nav-item" v-for="item in items" :key="item.link"><a :href="item.link">{{ item.name }}</a></li>
    </ul>
  </nav>
</template>

<style scoped>
.nav {
  background-color: var(--primary-background);
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 3rem;
}

.list {
  list-style: none;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 80%;
  padding: 0px;
}

.nav-item {
  height: 36px;
}

.nav-item a {
  display: flex;
  align-items: center;
  display: flex;
  width: 100% !important;
  height: 100%;
  padding-inline: 20px;
  border-radius: 4px;
  transition: 200ms;
  font-weight: 600;
}

.nav-item a:hover {
  cursor: pointer;
  background-color: var(--primary-background-light);
}

@media (max-width: 900px) {
  .nav {
    height: auto;
  }

  .list {
    flex-direction: column;
    align-items: center;
  }

  .nav-item {
    width: 100%;
    text-align: center;
  }

  .nav-item a {
    width: 100%;
    text-align: center;
  }
}
</style>