<template>
  <h1>Tracked Animals</h1>
  <List v-if="animals" :animals="animals" />
</template>

<script setup lang="ts">
import List from "@/components/List.vue";
import type { Animals } from "@/util/customTypes";
import { ref } from "vue";

const animals = ref<Animals>()

fetch('http://127.0.0.1:8000/api/v1/tracker/animals', {
  method: 'GET'
})
  .then((response) => {
    response.json().then((data) => {
      animals.value = data
    })
  })
  .catch((err) => {
    console.error(err)
  })</script>
