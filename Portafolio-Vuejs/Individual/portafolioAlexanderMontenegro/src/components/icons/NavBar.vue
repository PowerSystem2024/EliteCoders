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
    background-color: #4B0082;
    color: #000;
    padding: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 8px;
    margin: 1rem;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.navbar:hover {
    transform: scale(1.02);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
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
    overflow: hidden;
}

.navbar ul.active {
    max-height: 300px;
}

.nav-item {
    color: #DDA0DD;
    padding: 0.5rem 1rem;
    margin: 0 1rem;
    border: 2px solid transparent;
    border-radius: 4px;
    transition: background-color 0.3s, box-shadow 0.3s;
    text-decoration: none;
    background-color: rgba(75, 0, 130, 0.8);
}


.nav-item:hover {
    background-color: rgba(255, 255, 255, 0.2);
    border: 2px solid rgba(221, 160, 221, 0.5);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.menu-toggle {
    background: none;
    border: none;
    color: #DDA0DD;
    font-size: 1.5rem;
    cursor: pointer;
    display: none;
}

@media (max-width: 768px) {
    .navbar ul {
        display: none;
        flex-direction: column;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background-color: #4B0082;
        z-index: 10;
    }

    .navbar ul.active {
        display: flex;
    }

    .menu-toggle {
        display: block;
    }
}
</style>

