<script setup>
import CustomFooter from './components/CustomFooter.vue';
import Education from './components/Education.vue';
import Experience from './components/Experience.vue';
import NavBar from './components/NavBar.vue';
import Presentation from './components/Presentation.vue';
import Skills from './components/Skills.vue';
</script>

<template>
  <div class="container">
    <header>
      <NavBar />
    </header>

    <main>
      <Presentation />
      <Education />
      <Experience />
      <Skills />
      <CustomFooter />
    </main>
  </div>
</template>

<style lang="css">
.container {
  width: 100%;
  margin: 0px;
}
</style>