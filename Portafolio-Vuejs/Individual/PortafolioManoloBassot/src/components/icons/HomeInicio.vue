<script setup>
    const title = "Hello, I'm Manolo Bassot";
    const subtitle = "Electrician Technician & Software Developer(in progress)";
    const from = "San Rafael, Mendoza, Argentina";
    const presentation = "I am a programming technician with knowledge in software development, electrical systems, and experience in customer service. I adapt quickly to new areas and have skills in sales and teamwork. I am seeking to develop in the field of cybersecurity.";
</script>

<template>
    <section class="home-inicio">
        <div class="home-inicio-container">
            <h1>{{ title }}</h1>
            <h2>{{ subtitle }}</h2>
            <h3>{{ from }}</h3>
            <p>{{ presentation }}</p>
        </div>
    </section>
</template>

<style scoped>
.home-inicio {
    background-color: #333; /* Fondo gris claro */
    padding: 2rem; /* Espaciado interno */
    display: flex;
    justify-content: center; /* Centrar el contenido horizontalmente */
    align-items: center; /* Centrar el contenido verticalmente */
    min-height: 10vh; /* Ocupa toda la altura de la ventana */
    text-align: center; /* Centrar el texto */
    
}

.home-inicio-container {
    max-width: 6000px; /* Ancho máximo para el contenedor */
    background-color: #007bff; /* Fondo azul eléctrico */
    color: #ccc; /* Color del texto en blanco */
    padding: 2rem; /* Espaciado interno del contenedor */
    border-radius: 8px; /* Esquinas redondeadas */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Sombra sutil */
    width: 90%; /* Ancho del contenedor en pantallas pequeñas */
}

.home-inicio h1 {
    font-size: 2.5rem; /* Tamaño del título principal */
    margin-bottom: 1rem; /* Espaciado inferior */
}

.home-inicio h2 {
    font-size: 1.75rem; /* Tamaño del subtítulo */
    margin-bottom: 0.5rem; /* Espaciado inferior */
}

.home-inicio h3 {
    font-size: 1.25rem; /* Tamaño de la localidad */
    margin-bottom: 1rem; /* Espaciado inferior */
    font-weight: normal; /* Peso normal para la localidad */
}

.home-inicio p {
    font-size: 1rem; /* Tamaño del texto de presentación */
    line-height: 1.5; /* Altura de línea para mejor legibilidad */
}

/* Consultas de medios para hacer la sección más responsiva */
@media (max-width: 768px) {
    .home-inicio-container {
        padding: 1.5rem; /* Espaciado interno reducido en pantallas pequeñas */
    }

    .home-inicio h1 {
        font-size: 2rem; /* Tamaño del título principal reducido */
    }

    .home-inicio h2 {
        font-size: 1.5rem; /* Tamaño del subtítulo reducido */
    }

    .home-inicio h3 {
        font-size: 1.1rem; /* Tamaño de la localidad reducido */
    }

    .home-inicio p {
        font-size: 0.9rem; /* Tamaño del texto de presentación reducido */
    }
}

@media (max-width: 480px) {
    .home-inicio-container {
        padding: 1rem; /* Espaciado interno aún más reducido en pantallas muy pequeñas */
    }

    .home-inicio h1 {
        font-size: 1.5rem; /* Tamaño del título principal muy reducido */
    }

    .home-inicio h2 {
        font-size: 1.25rem; /* Tamaño del subtítulo muy reducido */
    }

    .home-inicio h3 {
        font-size: 1rem; /* Tamaño de la localidad muy reducido */
    }

    .home-inicio p {
        font-size: 0.85rem; /* Tamaño del texto de presentación muy reducido */
    }
}

</style>