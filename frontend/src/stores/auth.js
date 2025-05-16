import { defineStore } from "pinia";
import { useAuth, useUser } from "@clerk/vue";
import { watchEffect } from "vue";

export const useAuthStore = defineStore("auth", () => {
  const { isSignedIn, session, signOut } = useAuth();
  const user = useUser();

  // Expose reactive refs to components
  return {
    isSignedIn,
    session,
    user,
    signOut,
  };
});
