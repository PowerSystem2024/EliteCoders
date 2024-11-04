<script setup>
  import NavBar from './components/icons/NavBar.vue';
  import HomeInicio from './components/icons/HomeInicio.vue';
  import StudiesSection from './components/icons/StudiesSection.vue';
  import ProjectsSection from './components/icons/ProjectsSection.vue';
  import ContactSection from './components/icons/ContactSection.vue';
</script>

<template>
  <header>
    <!--Barra de Navegacion-->
    <NavBar />

  </header>
  <!--Contenido Principal-->
  <main>
    <router-view />
    <section id="home">
      <HomeInicio />
    </section>
    <section id="studies">
      <StudiesSection />
    </section>
    <section id="projects">
      <ProjectsSection />
    </section>
  </main>
  <!--Footer-->
  <section id="contact">
    <ContactSection />
  </section>
</template>

<style scoped>

</style>
