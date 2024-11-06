<script setup>
import NavBar from './components/icons/NavBar.vue';

import DatosGrupo from './components/icons/DatosGrupo.vue';
import IntegrantesGrupo from './components/icons/IntegrantesGrupo.vue';

import ProyectoComponente from './components/icons/ProyectoComponente.vue';
//puro js

</script>

<template>
  <header>
    <!--Barra de Navegacion-->
    <NavBar />
    
  </header>

  <main>
    <!-- El estilo de css de section se encuentra en base.cc-->
    <section id="inicio">
      <!-- Componente del grupo-->
    <DatosGrupo />
    </section>

    <section id="integrantes">
      <h2>Integrantes</h2>
      <!-- Componente de integrantes-->
      <IntegrantesGrupo />
    </section>

    <section id="proyectos">
      <h2>Proyectos</h2>
      <!-- Componente de Proyectos-->
    <ProyectoComponente />
    </section>

    <section id="habilidades">
      <h2>Habilidades</h2>
    </section>
  </main>

</template>

<style scoped>

        

</style>
