<template>
       <nav class="navbar">
        <div class="navbar-menu">
          <ul>
        <li><a href="#educacion" class="navbar-item">Educación</a></li>
        <li><a href="#experiencia" class="navbar-item">Experiencia</a></li>
        <li><a href="#proyectos" class="navbar-item">Proyectos</a></li>
        <li><a href="#habilidades" class="navbar-item">Habilidades</a></li>
      </ul>
    </div>
    </nav>
</template>

<script setup>
// cualquier lógica o importaciones
</script>

<style scoped>
/* Estilos para tu barra de navegación */
.navbar {
  background-color: #333;
  padding: 10px;
}
.navbar-menu ul {
  list-style: none;
  display: flex;
  gap: 15px;
}
.navbar-item {
  color: white;
  text-decoration: none;
}
.navbar-item:hover {
  text-decoration: underline;
}






</style>