<template>
    <footer class="footer">
      <div class="contact-container">
        <h3>Contact Me</h3>
        <div class="social-buttons">
          <!-- Botón WhatsApp -->
          <a
            :href="whatsappUrl"
            target="_blank"
            class="social-button"
            aria-label="WhatsApp"
          >
            <i class="fab fa-whatsapp"></i>
          </a>
  
          <!-- Botón LinkedIn -->
          <a
            href="https://www.linkedin.com/in/manolo-bassot-a682531b5/"
            target="_blank"
            class="social-button"
            aria-label="LinkedIn"
          >
            <i class="fab fa-linkedin"></i>
          </a>
  
          <!-- Botón GitHub -->
          <a
            href="https://github.com/manolobassot"
            target="_blank"
            class="social-button"
            aria-label="GitHub"
          >
            <i class="fab fa-github"></i>
          </a>
  
          <!-- Botón Instagram -->
          <a
            href="https://www.instagram.com/mbassot/?hl=es"
            target="_blank"
            class="social-button"
            aria-label="Instagram"
          >
            <i class="fab fa-instagram"></i>
          </a>
  
          <!-- Botón Telegram -->
          <a
            :href="telegramUrl"
            target="_blank"
            class="social-button"
            aria-label="Telegram"
          >
            <i class="fab fa-telegram-plane"></i>
          </a>
        </div>
  
        <p class="location">
          <i class="fas fa-map-marker-alt"></i> San Rafael, Mendoza, Argentina
        </p>
      </div>
  
      <div class="copyright">
        <p>&copy; 2024 Manolo Bassot. Todos los derechos reservados.</p>
      </div>
    </footer>
</template>
  
<script>
  export default {
    data() {
      return {
        whatsappUrl: "https://wa.me/5492604845171",
        telegramUrl: "https://t.me/Manolobassot", 
      };
    },
  };
</script>

<style scoped>
/* Estilo general del footer */
.footer {
  background-color: #222;
  color: #ccc;
  padding: 2rem;
  text-align: center;
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
  background-color: #444;
  color: white;
  border: none;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  transition: background-color 0.3s;
}

.social-button:hover {
  background-color: #666;
}

/* Íconos */
.social-button i {
  font-size: 1.5rem;
}

/* Estilo de la ubicación */
.location {
  margin-top: 1rem;
  font-size: 1.1rem;
}

/* Derechos reservados */
.copyright {
  margin-top: 2rem;
  font-size: 0.9rem;
  opacity: 0.8;
}

</style>
  