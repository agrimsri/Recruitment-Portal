// src/router/index.ts
import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth"; // import your auth store
import { useAuth } from "@clerk/vue";
import LandingView from "@/views/LandingView.vue";
import Dashboard from "@/views/Dashboard.vue";

export const routes = [
  { path: "/", component: LandingView },
  {
    path: "/dashboard",
    component: Dashboard,
    meta: { requiresAuth: true },
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("@/views/SignUpIn.vue"),
    meta: { requiresAuth: false },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to) => {
  const { isSignedIn } = useAuth();

  if (to.meta.requiresAuth && !isSignedIn.value) {
    return { path: "/" }; // redirect to Clerk’s sign-in page
  }
});

export default router;
