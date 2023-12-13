<template>
  <div class="container" v-if="animal">
    <div>
      <h1>Your tracked animal</h1>
      <p v-for="it in animal">
        {{ it }}
      </p>
    </div>
    <div>
      <div class="btn-group">
        <button class="btn btn-danger" @click="deleteDataset">
          Delete Animal
        </button>
        <button class="btn btn-primary" @click="getDataset">
          {{ weightData ? "Refresh weight data" : "Load weight data" }}
        </button>
      </div>
      <Weight
        v-if="weightData"
        :data="weightData"
        :created="created"
        :aId="animal.id"
        @added-weight="getDataset"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRoute } from "vue-router";
import type { Animal } from "@/util/customTypes";
import Weight from "@/components/Weight.vue";
import router from "@/router";

// vars
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

const deleteDataset = () => {
  if (!animal.value) {
    console.warn("No Animal Data found");
    return;
  }

  fetch("http://127.0.0.1:8000/api/v1/tracker/animal?id=" + animal.value.id, {
    method: "DELETE",
  })
    .then((response) => {
      response.json().then((data) => {
        console.log(data);
      });
    })
    .catch((err) => {
      console.error(err);
    });

  router.push("/animals");
};
</script>
