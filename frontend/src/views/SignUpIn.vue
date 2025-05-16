<template>
  <main class="flex items-center justify-center min-h-screen py-8">
    <component :is="currentComponent" />
  </main>
</template>

<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import SignIn from "@/components/SignIn.vue";
import Signup from "@/components/Signup.vue";

const route = useRoute();

const currentComponent = computed(() => {
  return route.path === "/signin" ? SignIn : Signup;
});
</script>
