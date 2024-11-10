<script setup>
    const title = "Hello, I'm Alexander Montenegro";
    const subtitle = "Student of Software Development, Systems and Telecommunications";
    const presentation = "I am studying software development and telecommunications. I am very interested in cybersecurity and my goal is to make a living out of it.";
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
    background-color: #333;
    padding: 2rem;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 10vh;
    text-align: center;
}

.home-inicio-container {
    max-width: 600px;
    background-color: #4B0082;
    color: #000;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    width: 90%;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}


.home-inicio-container:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

.home-inicio h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #000;
}

.home-inicio h2 {
    font-size: 1.75rem;
    margin-bottom: 0.5rem;
    color: #DDA0DD;
}

.home-inicio h3 {
    font-size: 1.25rem;
    margin-bottom: 1rem;
    font-weight: normal;
    color: #DDA0DD;
}

.home-inicio p {
    font-size: 1rem;
    line-height: 1.5;
    color: #E6E6FA;
}


@media (max-width: 768px) {
    .home-inicio-container {
        padding: 1.5rem;
    }

    .home-inicio h1 {
        font-size: 2rem;
    }

    .home-inicio h2 {
        font-size: 1.5rem;
    }

    .home-inicio h3 {
        font-size: 1.1rem;
    }

    .home-inicio p {
        font-size: 0.9rem;
    }
}

@media (max-width: 480px) {
    .home-inicio-container {
        padding: 1rem;
    }

    .home-inicio h1 {
        font-size: 1.5rem;
    }

    .home-inicio h2 {
        font-size: 1.25rem;
    }

    .home-inicio h3 {
        font-size: 1rem;
    }

    .home-inicio p {
        font-size: 0.85rem;
    }
}
</style>
