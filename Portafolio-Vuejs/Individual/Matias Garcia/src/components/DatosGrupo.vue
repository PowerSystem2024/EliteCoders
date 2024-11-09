<script setup>
const title = "Matias Garcia - EliteCoders";
const subtitle = "Estudiante de la UTN Tecnicatura Universitaria en Programación";
const presentacion = "¡Bienvenido a mi portafolio personal! Soy un estudiante de la Tecnicatura en Programación, unido a una pasión por la tecnología y el desarrollo de software util. Aquí encontraras mis proyectos, conocimientos y el esfuerzo en cada trabajo. ¡Gracias por visitarme!"
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
  background: linear-gradient(-45deg, #ff21bc, #ff7700, #f52f8e, #f2ff00);
  /* Fondo degradado */
  background-size: 400% 400%;
  animation: gradient 15s ease infinite;
  padding: 20px;
  box-sizing: border-box;
  border-radius: 12px;
  transition: background-color 0.3s, box-shadow 0.3s;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

.datos-grupo:hover {
  background-color: #1a1a1a;
  /* Fondo negro más claro al pasar el cursor */
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  /* Sombra más pronunciada */
}

.card {
  background-color: #875a8f;
  /* Fondo blanco para la tarjeta */
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  /* Sombra suave */
  max-width: 600px;
  text-align: center;
  transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  /* Sombra más pronunciada al pasar el cursor */
}

.card h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
  color: #86d4fe;
  /* Azul oscuro */
}

.card h2 {
  font-size: 1.5rem;
  margin-bottom: 20px;
  color: #9bd0fa;
  /* Azul intermedio */
}

.card p {
  font-size: 1rem;
  line-height: 1.6;
  color: #ffffff;
  /* Texto negro suave */
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
