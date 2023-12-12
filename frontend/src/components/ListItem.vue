<template>
  <tr @click="goToAnimal">
    <td>{{ item.name }}</td>
    <td>{{ item.species }}</td>
    <td>{{ item.sex }}</td>
    <td>{{ item.weight }}</td>
    <td>{{ item.birthday }}</td>
    <td>{{ item.created }}</td>
  </tr>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter()

const props = defineProps<{
  item: any
}>()

const goToAnimal = () => {
  router.push("/animals/" + props.item.id)
}
</script>

<style scoped>
tr:hover {
  cursor: pointer;
  background-color: #ccc;
}
</style>
