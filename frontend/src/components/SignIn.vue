<template>
  <div
    class="bg-base-200 py-8 px-12 rounded-2xl shadow-lg w-lg flex justify-center items-center"
  >
    <div class="w-full">
      <h2 class="text-3xl font-bold text-center mb-8 text-base-content">
        Welcome Back
      </h2>

      <div v-if="!isLoaded" class="flex justify-center items-center">
        <span class="loading loading-spinner loading-xl"></span>
      </div>
      <div v-else>
        <div class="card bg-base-100 shadow-xl">
          <form @submit.prevent="handleSubmit" class="card-body">
            <div class="form-control">
              <label class="label" for="email">
                <span class="label-text">Email address</span>
              </label>
              <input
                id="email"
                v-model="emailAddress"
                type="email"
                autocomplete="email"
                required
                class="input input-bordered w-full"
              />
            </div>

            <div class="form-control">
              <label class="label" for="password">
                <span class="label-text">Password</span>
              </label>
              <input
                id="password"
                v-model="password"
                type="password"
                autocomplete="current-password"
                required
                class="input input-bordered w-full"
              />
            </div>

            <div v-if="error" class="alert alert-error mt-4">
              {{ error }}
            </div>

            <div class="form-control mt-6 text-center">
              <button
                type="submit"
                :disabled="loading"
                class="btn btn-primary"
                :class="{ loading: loading }"
              >
                {{ loading ? "Signing in..." : "Sign in" }}
              </button>
            </div>

            <div class="text-center mt-4">
              <RouterLink to="/signup" class="text-primary hover:underline">
                Don't have an account? Sign up
              </RouterLink>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useSignIn, useUser } from "@clerk/vue";

const router = useRouter();
const { signIn, isLoaded, setActive } = useSignIn();
const { user } = useUser();

// Form data
const emailAddress = ref("");
const password = ref("");

// UI state
const error = ref("");
const loading = ref(false);

const handleSubmit = async () => {
  if (!isLoaded.value) return;

  try {
    loading.value = true;
    error.value = "";

    const result = await signIn.value.create({
      identifier: emailAddress.value,
      password: password.value,
    });

    if (result.status === "complete") {
      await setActive.value({ session: result.createdSessionId });

      // Reload user to get latest metadata
      if (user.value) {
        await user.value.reload();
      }

      // Route based on user role
      const userRole = user.value?.publicMetadata?.role;
      if (userRole === "recruiter") {
        router.push("/recruiter-dashboard");
      } else if (userRole === "candidate") {
        router.push("/candidate-dashboard");
      } else {
        router.push("/dashboard");
      }
    } else {
      error.value = `Sign in failed: ${result.status}`;
    }
  } catch (err) {
    console.error("Error during sign in:", err);
    error.value = "Invalid email or password";
  } finally {
    loading.value = false;
  }
};
</script>
