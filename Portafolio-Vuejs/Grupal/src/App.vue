<script setup>
import NavBar from './components/NavBar.vue';
import DatosGrupo from './components/DatosGrupo.vue';
import IntegrantesGrupo from './components/IntegrantesGrupo.vue';
import ProyectoComponente from './components/ProyectoComponente.vue';
import Intereses from './components/Intereses.vue';
import Habilidades from './components/Habilidades.vue';
import CustomFooter from './components/CustomFooter.vue'

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
      <Habilidades />
    </section>

    <section id="intereses">
      <!--Componente Intereses-->
      <h2>Intereses</h2>
      <Intereses />
    </section>

  </main>
  <CustomFooter />
</template>
