// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import LandingView from "@/views/LandingView.vue";

export const routes = [
  { path: "/", component: LandingView },
  {
    path: "/recruiter-dashboard",
    component: () => import("@/views/RecruiterDashboard.vue"),
    name: "RecruiterDashboard",
    meta: { requiresAuth: true, role: "recruiter" },
  },
  {
    path: "/candidate-dashboard",
    component: () => import("@/views/CandidateDashboard.vue"),
    name: "CandidateDashboard",
    meta: { requiresAuth: true, role: "candidate" },
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
      case "recruiter":
        return { path: "/recruiter-dashboard" };
      case "candidate":
        return { path: "/candidate-dashboard" };
      default:
        return { path: "/" };
    }
  }
});

export default router;
