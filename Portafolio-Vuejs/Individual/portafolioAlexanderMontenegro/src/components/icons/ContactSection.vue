<template>
    <footer class="footer">
      <div class="contact-container">
        <h3>Contact Me</h3>
        <div class="social-buttons">
          <!-- Botón LinkedIn -->
          <a
            href="https://www.linkedin.com/in/alex-montenegro-aaa178304/"
            target="_blank"
            class="social-button"
            aria-label="LinkedIn"
          >
            <i class="fab fa-linkedin"></i>
          </a>

          <!-- Botón GitHub -->
          <a
            href="https://github.com/AlexMS7"
            target="_blank"
            class="social-button"
            aria-label="GitHub"
          >
            <i class="fab fa-github"></i>
          </a>

          <!-- Botón Instagram -->
          <a
            href="https://www.instagram.com/aleex.mn/"
            target="_blank"
            class="social-button"
            aria-label="Instagram"
          >
            <i class="fab fa-instagram"></i>
          </a>


        </div>

        <p class="location">
          <i class="fas fa-map-marker-alt"></i> San Rafael, Mendoza, Argentina
        </p>
      </div>

      <div class="copyright">
        <p>&copy; Alexander Montenegro todos los derechos reservados.</p>
      </div>
    </footer>
</template>

<style scoped>

.footer {
  background-color: #222;
  color: #4B0082;
  padding: 2rem;
  text-align: center;
  font-family: Arial, sans-serif;
}

.contact-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

/* Botones de redes sociales */
.social-buttons {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.social-button {
  background-color: #333;
  color: #4B0082;
  border: 2px solid #4B0082;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  transition: background-color 0.3s, color 0.3s;
}

.social-button:hover {
  background-color: #4B0082;
  color: black;
}


.social-button i {
  font-size: 1.5rem;
}


.location {
  margin-top: 1rem;
  font-size: 1.1rem;
  color: #4B0082;
}


.copyright {
  margin-top: 2rem;
  font-size: 0.9rem;
  color: #796e81;
  opacity: 0.8;
}

</style>

