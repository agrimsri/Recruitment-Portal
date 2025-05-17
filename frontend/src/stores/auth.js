import { defineStore } from "pinia";
import { ref, computed, watch } from "vue";
import { useAuth, useUser } from "@clerk/vue";

export const useAuthStore = defineStore("auth", () => {
  const isInitialized = ref(false);
  const isAuthenticated = ref(false);
  const userRole = ref(null);
  const userId = ref(null);

  const { isSignedIn, isLoaded } = useAuth();
  const { user, isLoaded: isUserLoaded } = useUser();

  // Getters
  const isReady = computed(() => isInitialized.value);
  const getRole = computed(() => userRole.value);

  // Actions
  async function initialize() {
    if (isInitialized.value) return;

    // Wait for Clerk to initialize
    await new Promise((resolve) => {
      const checkLoaded = () => {
        if (isLoaded.value && isUserLoaded.value) {
          resolve();
        } else {
          setTimeout(checkLoaded, 50);
        }
      };
      checkLoaded();
    });

    // Setup auth state watchers
    watch(
      isSignedIn,
      (newIsSignedIn) => {
        isAuthenticated.value = newIsSignedIn;
        if (!newIsSignedIn) {
          userRole.value = null;
          userId.value = null;
        }
      },
      { immediate: true }
    );

    // Setup user state watchers
    watch(
      () => user.value?.publicMetadata?.role,
      (newRole) => {
        userRole.value = newRole || null;
      },
      { immediate: true }
    );

    watch(
      () => user.value?.id,
      (newId) => {
        userId.value = newId || null;
      },
      { immediate: true }
    );

    isInitialized.value = true;
  }

  async function waitForInitialization() {
    if (isInitialized.value) return;

    await new Promise((resolve) => {
      const checkInitialized = () => {
        if (isInitialized.value) {
          resolve();
        } else {
          setTimeout(checkInitialized, 50);
        }
      };
      checkInitialized();
    });
  }

  return {
    // State
    isInitialized,
    isAuthenticated,
    userRole,
    userId,

    // Getters
    isReady,
    getRole,

    // Actions
    initialize,
    waitForInitialization,
  };
});
