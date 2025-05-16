import { defineStore } from "pinia";
import { useAuth, useUser } from "@clerk/vue";
import { ref, watchEffect } from "vue";

export const useAuthStore = defineStore("auth", () => {
  const { isSignedIn, session, signOut } = useAuth();
  const { user } = useUser();

  const userRole = ref(null);

  // Watch for changes in user data and update role
  watchEffect(() => {
    if (user.value?.isLoaded) {
      userRole.value = user.value?.publicMetadata?.role || null;
    }
  });

  const getUserRole = () => {
    return userRole.value;
  };

  // Expose reactive refs and methods to components
  return {
    isSignedIn,
    session,
    user,
    signOut,
    userRole,
    getUserRole,
  };
});
