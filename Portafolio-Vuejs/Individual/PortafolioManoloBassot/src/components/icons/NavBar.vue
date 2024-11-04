<script setup>
import { ref } from 'vue';

const menu = ref([
    { id: 1, name: 'Home', href: '#home' },
    { id: 2, name: 'Studies', href: '#studies' },
    { id: 3, name: 'Projects', href: '#projects' },
    { id: 4, name: 'Contact', href: '#contact' },
]);

const isMobileMenuOpen = ref(false);
const scrollToSection = (href) => {
    const section = document.querySelector(href);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
        isMobileMenuOpen.value = false; // Cerrar menú móvil al seleccionar una opción
    }
};
</script>

<template>
    <nav class="navbar">
        <div class="navbar-menu">
            <button class="menu-toggle" @click="isMobileMenuOpen = !isMobileMenuOpen">
                &#9776; <!-- Icono de menú hamburguesa -->
            </button>
            <ul :class="{ 'active': isMobileMenuOpen }">
                <li v-for="nav in menu" :key="nav.id">
                    <a :href="nav.href" class="nav-item" @click.prevent="scrollToSection(nav.href)">{{ nav.name }}</a>
                </li>
            </ul>
        </div>
    </nav>
</template>

<style scoped>
.navbar {
    background-color: #007bff; /* Azul eléctrico */
    color: white;
    padding: 1rem;
    display: flex;
    justify-content: center; /* Centrar elementos en la navbar */
    align-items: center;
    border-radius: 8px; /* Esquinas redondeadas en la navbar */
    margin: 1rem; /* Margen para separar de otros elementos */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Sombra sutil */
}

.navbar-menu {
    display: flex;
    align-items: center;
}

.navbar ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    transition: max-height 0.3s ease-in;
    overflow: hidden; /* Para animar el menú al abrir/cerrar */
    
}

.navbar ul.active {
    max-height: 300px; /* Mostrar el menú cuando está activo */
}

.nav-item {
    color: #ccc; /* Cambia el color del texto a blanco para que sea más visible */
    padding: 0.5rem 1rem; /* Espaciado interior de los enlaces */
    margin: 0 1rem; /* Espacio entre los botones */
    border: 2px solid transparent; /* Borde transparente por defecto */
    border-radius: 4px; /* Esquinas redondeadas en los enlaces */
    transition: background-color 0.3s, box-shadow 0.3s; /* Transición para el hover */
    text-decoration: none; /* Eliminar subrayado */
    background-color: rgba(0, 123, 255, 0.8); /* Fondo azul semitransparente */
}

/* Estilo del botón al pasar el ratón */
.nav-item:hover {
    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semitransparente al pasar el ratón */
    border: 2px solid rgba(255, 255, 255, 0.5); /* Borde visible al hacer hover */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Sombra al hacer hover */
}

.menu-toggle {
    background: none;
    border: none;
    color: white;
    font-size: 1.5rem; /* Tamaño del icono de menú */
    cursor: pointer;
    display: none; /* Oculto por defecto */
}

@media (max-width: 768px) {
    .navbar ul {
        display: none; /* Ocultar el menú en pantallas pequeñas */
        flex-direction: column; /* Cambiar a columna en pantallas pequeñas */
        position: absolute;
        top: 100%; /* Alinear con el borde inferior de la navbar */
        left: 0;
        right: 0;
        background-color: #007bff; /* Fondo azul eléctrico */
        z-index: 10; /* Asegurarse de que esté por encima de otros elementos */
    }

    .navbar ul.active {
        display: flex; /* Mostrar el menú cuando está activo */
    }

    .menu-toggle {
        display: block; /* Mostrar el botón de menú hamburguesa en pantallas pequeñas */
    }
}


</style>
