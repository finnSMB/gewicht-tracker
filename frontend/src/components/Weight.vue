<template>
  <div>
    <div>
      <h2>Add data</h2>
      <div class="input-group mb-3">
        <input
          aria-describedby="button-addon1"
          placeholder="Weight (in KG)"
          id="weight"
          type="number"
          class="form-control"
          :class="{ 'error-border': v$.weight.$error }"
          v-model="weight"
        />
        <button
          type="button"
          class="btn btn-primary"
          id="button-addon1"
          @click="submitWeight"
          @submit="submitWeight"
        >
          Add
        </button>
        <span v-if="v$.weight.$error" style="color: red">
          <span v-if="v$.weight.required">Weight required</span>
        </span>
      </div>
    </div>
    <div class="chart">
      <h2>Chart</h2>
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
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

const emit = defineEmits<{
  (e: 'added-weight'): void
}>()

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

  emit("added-weight")
};
</script>

<style scoped>
.chart {
  padding-bottom: 100px;
}
</style>
