import "./assets/css/main.css";

import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import { clerkPlugin } from "@clerk/vue";
import { dark } from "@clerk/themes";

const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY;

const app = createApp(App);

app.use(clerkPlugin, {
  publishableKey: PUBLISHABLE_KEY,
  appearance: { baseTheme: dark },
});
app.use(createPinia());
app.use(router);

app.mount("#app");
