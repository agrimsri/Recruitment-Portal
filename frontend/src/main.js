import "./assets/css/main.css";

import { createApp } from "vue";
import { createPinia } from "pinia";
import { clerkPlugin } from "@clerk/vue";
import { dark } from "@clerk/themes";

import App from "./App.vue";
import router from "./router";
import { useAuthStore } from "./stores/auth";

const app = createApp(App);
const pinia = createPinia();

// Initialize Pinia first
app.use(pinia);

// Initialize Clerk
app.use(clerkPlugin, {
  publishableKey: import.meta.env.VITE_CLERK_PUBLISHABLE_KEY,
  appearance: { baseTheme: dark },
});

// Initialize auth store
const authStore = useAuthStore();
await authStore.initialize();

// Initialize router last
app.use(router);

app.mount("#app");
