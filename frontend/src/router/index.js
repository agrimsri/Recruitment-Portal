// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth";
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
  const auth = useAuthStore();

  // Wait for auth store to initialize
  await auth.waitForInitialization();

  // Allow access to non-auth routes
  if (!to.meta.requiresAuth) {
    return;
  }

  // Redirect to signin if not authenticated
  if (!auth.isAuthenticated) {
    return { path: "/signin" };
  }

  // Handle role-based access
  const userRole = auth.userRole;

  // If route requires specific role and user's role doesn't match
  if (to.meta.role && userRole !== to.meta.role) {
    // Redirect to appropriate dashboard based on role
    switch (userRole) {
      case "hr":
        return { path: "/hr-dashboard" };
      case "user":
        return { path: "/user-dashboard" };
      default:
        return { path: "/" };
    }
  }
});

export default router;
