<template>
  <h1>This is an about page</h1>
  <p>No content yet.</p>

  <p v-if="animalsTracked">
    Animals tracked: <b>{{ animalsTracked.amount }}</b>
  </p>
</template>

<script setup lang="ts">
import { ref } from "vue";

const animalsTracked = ref<number>();

fetch("http://127.0.0.1:8000/api/v1/tracker/amount")
  .then((response) => {
    response.json().then((data) => {
      animalsTracked.value = data[0];
    });
  })
  .catch((err) => {
    console.error(err);
  });
</script>
