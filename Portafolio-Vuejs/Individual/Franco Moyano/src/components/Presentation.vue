<script setup>

import CustomSection from './CustomSection.vue';
</script>

<template>
  <CustomSection id="presentation">
    <div class="presentation">
      <img src="../assets/profile-square.jpg" width="200" id="profile-photo">
      <hr />
      <div id="personal">
        <h1 id="title">Franco Moyano</h1>
        <span>Programador y estudiante 😁</span>
        <span>24 años</span>
        <span>franco.moyano.sr@gmail.com</span>
        <span>San Rafael, Mendoza, Argentina</span>
      </div>
    </div>
  </CustomSection>
</template>

<style scoped>
.presentation {
  display: flex;
  gap: 3rem;
}

#title {
  font-size: 40px;
  font-weight: 600;
}

#personal {
  display: flex;
  justify-content: center;
  flex-direction: column;
}

#profile-photo {
  border-radius: 50%;
}

@media (max-width: 1050px) {
  .presentation {
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
  }

  #title {
    line-height: 1.2;
  }

  #profile-photo {
    margin: auto;
  }

  hr {
    display: none;
  }
}
</style>
