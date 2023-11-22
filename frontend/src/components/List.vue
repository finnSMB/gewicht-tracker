<template>
  <table class="table">
    <thead>
      <tr>
        <th>Name</th>
        <th>Species</th>
        <th>Sex</th>
        <th>Weight</th>
        <th>Birthday</th>
        <th>Created</th>
      </tr>
    </thead>
    <tbody>
      <ListItem v-for="(item, key) in 1" :key="key" />
    </tbody>
  </table>
</template>

<script setup lang="ts">
import ListItem from "@/components/ListItem.vue";
</script>
