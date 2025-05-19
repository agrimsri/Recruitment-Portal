<template>
  <h1 class="text-7xl text-center">Candidate Dashboard</h1>
  <button
    @click="sendRequest"
    class="text-center btn btn-xs sm:btn-sm md:btn-md lg:btn-lg xl:btn-xl"
  >
    Responsive
  </button>
  {{ msg }}
  <pre>{{ user }}</pre>
</template>

<script setup>
import { ref } from "vue";
import { useUser } from "@clerk/vue";

const { user } = useUser();
const msg = ref("Initial");

const sendRequest = async () => {
  try {
    console.log(await Clerk.session.getToken());
    const response = await fetch(
      `${import.meta.env.VITE_BACKEND_URL}/api/test`,
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${await Clerk.session.getToken({
            template: "develop",
          })}`,
        },
      }
    );
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    msg.value = data.message;
  } catch (error) {
    console.error("Error sending request:", error);
  }
};
</script>
