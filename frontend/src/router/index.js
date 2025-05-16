// src/router/index.ts
import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { useAuth } from "@clerk/vue";
import { useUser } from "@clerk/vue";
import LandingView from "@/views/LandingView.vue";

export const routes = [
  { path: "/", component: LandingView },
  {
    path: "/hr-dashboard",
    component: () => import("@/views/HrDashboard.vue"),
    name: "HrDashboard",
    meta: { requiresAuth: true, role: "hr" },
  },
  {
    path: "/user-dashboard",
    component: () => import("@/views/UserDashboard.vue"),
    name: "UserDashboard",
    meta: { requiresAuth: true, role: "user" },
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("@/views/SignUpIn.vue"),
    meta: { requiresAuth: false },
  },
  {
    path: "/signin",
    name: "SignIn",
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
  const { user } = useUser();

  // If route requires auth and user is not signed in
  if (to.meta.requiresAuth && !isSignedIn.value) {
    return { path: "/signin" };
  }

  // If route has a role requirement and user's role doesn't match
  if (to.meta.role && user.value?.publicMetadata?.role !== to.meta.role) {
    // Redirect to appropriate dashboard based on user's role
    const userRole = user.value?.publicMetadata?.role;
    if (userRole === "hr") {
      return { path: "/hr-dashboard" };
    } else if (userRole === "user") {
      return { path: "/user-dashboard" };
    }
    return { path: "/" };
  }
});

export default router;
