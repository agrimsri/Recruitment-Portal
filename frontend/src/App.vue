<script setup>
import { RouterLink, RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue";
</script>

<template>
  <header>
    <Navbar />
  </header>
  <main class="min-h-[calc(100vh-4rem)]">
    <RouterView />
  </main>
</template>
