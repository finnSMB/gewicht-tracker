<template>
  <div>
    <div>
      <h2>Chart</h2>
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>

    <div>
      <h2>Add data</h2>
      <div class="mb-3">
        <label for="weight" class="form-label">Weight (in KG)</label>
        <input
          id="weight"
          type="number"
          class="form-control"
          :class="{ 'error-border': v$.weight.$error }"
          v-model="weight"
        />
        <span v-if="v$.weight.$error" style="color: red">
          <span v-if="v$.weight.required">Weight required</span>
        </span>
      </div>
      <button class="btn btn-primary" @click="submitWeight">Add</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";
import { ref } from "vue";
import { useVuelidate } from "@vuelidate/core";
import { required } from "@vuelidate/validators";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

const props = defineProps<{
  aId: number;
  data: any;
  created: any;
}>();

const weight = ref<number>();

const rules = {
  weight: { required },
};

const v$ = useVuelidate(rules, { weight });

const chartData = {
  labels: props.created,
  datasets: [{ data: props.data }],
};

const chartOptions = {
  responsive: true,
};

const submitWeight = () => {
  v$.value.$touch();
  if (v$.value.$error) {
    console.warn("Vuelidate error");
    return;
  }

  fetch("http://127.0.0.1:8000/api/v1/tracker/animalweight", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      weight: weight.value,
      id: props.aId,
    }),
  });

  window.location.reload()
};
</script>

<style></style>
