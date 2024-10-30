<script setup>
const title = "EliteCoders";
const subtitle = "Grupo de la UTN Tecnicatura Universitaria en Programación";
const presentacion = "¡Bienvenidos a nuestro portafolio grupal! Somos un equipo de estudiantes de la Tecnicatura en Programación, unidos por la pasión por la tecnología y el desarrollo de software. Aquí encontrarán nuestros proyectos, conocimientos y el esfuerzo que ponemos en cada trabajo. ¡Gracias por visitarnos!"
</script>

<template>
    <div class="datos-grupo">
        <div class="card">
            <h1>{{ title }}</h1>
            <h2>{{ subtitle }}</h2>
            <p>{{ presentacion }}</p>
        </div>
    </div>
</template>


<style scoped>
.datos-grupo {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 75vh;
  background-color: #202020; /* Celeste claro de fondo */
  padding: 20px;
  box-sizing: border-box;
  border-radius: 12px;
}

.card {
  background-color: #ffffff; /* Fondo blanco para la tarjeta */
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Sombra suave */
  max-width: 600px;
  text-align: center;
}

.card h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
  color: #0277bd; /* Azul oscuro */
}

.card h2 {
  font-size: 1.5rem;
  margin-bottom: 20px;
  color: #01579b; /* Azul intermedio */
}

.card p {
  font-size: 1rem;
  line-height: 1.6;
  color: #333; /* Texto negro suave */
}

@media (max-width: 768px) {
  .card {
    padding: 20px;
  }

  .card h1 {
    font-size: 2rem;
  }

  .card h2 {
    font-size: 1.2rem;
  }

  .card p {
    font-size: 0.9rem;
  }
}
</style>
