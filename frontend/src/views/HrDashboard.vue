<template>
  <h1 class="text-7xl text-center">HR Dashboard</h1>
  <pre>{{ user }}</pre>
</template>

<script setup>
import { useUser } from "@clerk/vue";

const { user } = useUser();
</script>
