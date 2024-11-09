<template>
  <div class="container">
    <h3 class="title" v-if="title" :id="id">{{ title }}</h3>
    <div class="content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "CustomSection",
  props: {
    title: {
      type: String,
      required: false
    },
    id: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
.title {
  font-size: 22px;
}

.content {
  background-color: var(--color-background-light);
  padding: 2rem 5rem;
  border-radius: 7px;
  border: 3px solid var(--color-background);
  transition: 200ms;
}

.content:hover {
  border-color: var(--primary-background);
}

.container {
  width: 70%;
  margin: 2rem auto;
}

@media (max-width: 600px) {
  .container {
    width: 90%;
  }

  .content {
    padding: 1rem 1rem;
  }
}
</style>