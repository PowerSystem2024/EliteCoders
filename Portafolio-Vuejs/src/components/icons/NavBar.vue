<template>

      <nav class="navbar">
        <div class="navbar-logo">
          <img src="@/assets/logoGrupo.jpeg" alt="Logo"/>
        </div>
        <div class="navbar-menu">
          <ul>
            <a v-for="nav in navegacion" :key="nav.nombre" :href="nav.enlace" class="navbar-item">{{ nav.nombre }}</a>
          </ul>
        </div>
      </nav>
</template>

<script setup>
  import { ref } from 'vue';
  const navegacion = ref([
    {id:1, nombre: 'Inicio', enlace: '#inicio'},
    {id:2, nombre: 'Integrantes', enlace: '#integrantes'},
    {id:3, nombre: 'Proyectos', enlace: '#proyectos'},
    {id:4, nombre: 'Habilidades', enlace: '#habilidades'},
  ]);

</script>

<style scoped>
/* Barra de navegación */
.navbar {
  background-color: #01579b; /* Azul intermedio */
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px 30px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra suave */
  border-radius: 8px; /* Bordes redondeados */
  margin-bottom: 20px;
}

/* Logo */
.navbar-logo img {
  height: 50px;
  width: auto;
}

/* Menú de navegación */
.navbar-menu ul {
  list-style: none;
  display: flex;
  gap: 20px;
  margin: 0;
  padding: 0;
}

.navbar-menu li {
  display: inline;
}

/* Enlaces de navegación */
.navbar-item {
  color: #ffffff; /* Blanco para los enlaces */
  text-decoration: none;
  font-size: 1.1rem;
  font-weight: 500;
}

.navbar-item:hover {
  color: #e0f7fa; /* Celeste claro al pasar el cursor */
  text-decoration: underline;
}

/* Responsividad */
@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar-menu ul {
    flex-direction: column;
    gap: 10px;
  }

  .navbar-logo img {
    height: 40px;
  }
}

</style>