<template>
  <div class="content container">
    <header>
      <nav class="navbar-navbar">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/animals">Animals</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </header>

    <RouterView />
  </div>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped>
.content {
  -webkit-box-shadow: 0px 1px 11px -2px #000000;
  box-shadow: 0px 5px 5px -2px #898989;
  min-height: 100vh;
  background-color: #fbfbfb;
}

.error-border {
  border: 1px solid red;
  border-radius: 8px;
}

header {
  padding: 10px;
}

nav {
  width: 100%;
  text-align: center;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}
</style>
