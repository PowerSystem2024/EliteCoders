<script setup>
import NavBar from './components/icons/NavBar.vue';

import DatosGrupo from './components/icons/DatosGrupo.vue';
import IntegrantesGrupo from './components/icons/IntegrantesGrupo.vue';

//puro js

</script>

<template>
  <header>
    <!--Barra de Navegacion-->
    <NavBar />
    
  </header>

  <main>
    <section id="inicio">
    <DatosGrupo />
    </section>
    <section id="integrantes"><h2>Integrantes</h2>
      <IntegrantesGrupo />
    </section>
    <section id="proyectos"><h2>Proyectos</h2></section>
    <section id="habilidades"><h2>Habilidades</h2></section>
  </main>

</template>

<style scoped>

        

</style>
