<template>
  <div v-if="animal">
    <h1>{{ animal.name }}</h1>
    <p v-for="it in animal">
      {{ it }}
    </p>
    <br />
    <div class="row">
      <button v-if="!weightData" class="btn btn-primary" @click="getDataset">
        Load Weight Data
      </button>
      <Weight
        v-if="weightData"
        :data="weightData"
        :created="created"
        :aId="animal.id"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRoute } from "vue-router";
import type { Animal } from "@/util/customTypes";
import Weight from "@/components/Weight.vue";

const route = useRoute();
const animal = ref<Animal>();
const weightData = ref<any>();
const created = ref<any>();

fetch("http://127.0.0.1:8000/api/v1/tracker/animal?id=" + route.params.id, {
  method: "GET",
})
  .then((response) => {
    response.json().then((data) => {
      animal.value = data[0];
    });
  })
  .catch((err) => {
    console.error(err);
  });

const getDataset = () => {
  if (!animal.value) {
    console.warn("No Animal Data found");
    return;
  }

  fetch(
    "http://127.0.0.1:8000/api/v1/tracker/animalweight?id=" + animal.value.id,
    {
      method: "GET",
    }
  )
    .then((response) => {
      response.json().then((data) => {
        weightData.value = data.map((item: any) => item.weight);
        created.value = data.map((item: any) => item.created);
      });
    })
    .catch((err) => {
      console.error(err);
    });
};
</script>
