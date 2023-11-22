<template>
  <form>
    <div class="mb-3" v-if="!weightMode">
      <label for="name" class="form-label">Animal name</label>
      <input id="name" type="text" class="form-control" v-model="name" />
    </div>

    <div class="mb-3" v-if="!weightMode">
      <label for="species" class="form-label">Species</label>
      <input id="species" type="text" class="form-control" v-model="species" />
    </div>

    <div class="mb-3" v-if="!weightMode">
      <label for="sex" class="form-label">Sex</label>
      <select id="sex" class="form-select" v-model="sex">
        <option disabled value="">...</option>
        <option>Male</option>
        <option>Female</option>
      </select>
    </div>

    <div class="mb-3" v-if="!weightMode">
      <label for="date" class="form-label">Birthday</label>
      <input
        id="date"
        type="datetime-local"
        class="form-control"
        v-model="birthdate"
      />
    </div>

    <div class="mb-3">
      <label for="weight" class="form-label">Weight (in KG)</label>
      <input id="weight" type="number" class="form-control" v-model="weight" />
    </div>

    <button
      type="button"
      class="btn btn-primary d-grid gap-2 col-6 mx-auto"
      @click="submitForm"
    >
      Submit
    </button>
  </form>
</template>

<script setup lang="ts">
import { ref } from "vue";

const props = defineProps<{
  weightMode?: boolean;
}>();

const name = ref<string>("");
const species = ref<string>("");
const sex = ref<string>("");
const birthdate = ref<string>("");
const weight = ref<string>("");

const submitForm = () => {
  var values = [];
  if (props.weightMode) {
    values = [weight.value];
  } else {
    values = [name.value, species.value, sex.value, birthdate.value, weight.value];
  }

  console.log(values);
};
</script>
