<template>
  <h1>This is an about page</h1>
  <p>No content yet.</p>

  <p>Animals tracked: {{ animalsTracked }}</p>
</template>

<script setup lang="ts">
import { ref } from "vue";

const animalsTracked = ref<number>(0);

fetch("http://127.0.0.1/api/v1/tracker/amount")
  .then((response) => {
    response.json().then((data) => {
      animalsTracked.value = data;
    });
  })
  .catch((err) => {
    console.error(err);
  });
</script>
