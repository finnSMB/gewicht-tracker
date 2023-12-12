<template>
  <form>
    <div class="mb-3" v-if="!weightMode">
      <label for="name" class="form-label">Animal name</label>
      <input
        id="name"
        type="text"
        class="form-control"
        :class="{ 'error-border': v$.name.$error }"
        v-model="name"
      />
      <span v-if="v$.name.$error" style="color: red">
        <span v-if="v$.name.required">Name required</span>
        <span v-if="v$.name.minLength">Minimum length of 2</span>
      </span>
    </div>

    <div class="mb-3" v-if="!weightMode">
      <label for="species" class="form-label">Species</label>
      <input
        id="species"
        type="text"
        class="form-control"
        :class="{ 'error-border': v$.name.$error }"
        v-model="species"
      />
      <span v-if="v$.species.$error" style="color: red">
        <span v-if="v$.species.required">Species required</span>
      </span>
    </div>

    <div class="mb-3" v-if="!weightMode">
      <label for="sex" class="form-label">Sex</label>
      <select
        id="sex"
        class="form-select"
        :class="{ 'error-border': v$.name.$error }"
        v-model="sex"
      >
        <option disabled value="">...</option>
        <option>Male</option>
        <option>Female</option>
      </select>
      <span v-if="v$.sex.$error" style="color: red">
        <span v-if="v$.sex.required">Sex required</span>
      </span>
    </div>

    <div class="mb-3" v-if="!weightMode">
      <label for="date" class="form-label">Birthday</label>
      <input
        id="date"
        type="date"
        class="form-control"
        :class="{ 'error-border': v$.name.$error }"
        v-model="birthdate"
      />
      <span v-if="v$.birthdate.$error" style="color: red">
        <span v-if="v$.birthdate.required">Birthdate required</span>
      </span>
    </div>

    <div class="mb-3">
      <label for="weight" class="form-label">Weight (in KG)</label>
      <input
        id="weight"
        type="number"
        class="form-control"
        :class="{ 'error-border': v$.name.$error }"
        v-model="weight"
      />
      <span v-if="v$.weight.$error" style="color: red">
        <span v-if="v$.weight.required">Weight required</span>
      </span>
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
import { useVuelidate } from "@vuelidate/core";
import { required } from "@vuelidate/validators";

// Deprecated
const props = defineProps<{
  weightMode?: boolean;
}>();

const name = ref<string>("");
const species = ref<string>("");
const sex = ref<string>("");
const birthdate = ref<string>("");
const weight = ref<string>("");

const rules = {
  name: { required },
  species: { required },
  sex: { required },
  birthdate: { required },
  weight: { required },
};

const v$ = useVuelidate(rules, { name, species, sex, birthdate, weight });

const submitForm = () => {
  v$.value.$touch();
  if (v$.value.$error) {
    return;
  }

  fetch("http://127.0.0.1:8000/api/v1/tracker/animal", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: getValues(),
  });
};

const getValues = () => {
  return JSON.stringify({
    name: name.value.toString(),
    species: species.value.toString(),
    sex: sex.value.toLowerCase().toString(),
    birthday: birthdate.value.toString(),
    weight: weight.value,
  });
};
</script>

