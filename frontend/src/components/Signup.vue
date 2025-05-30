<template>
  <div
    class="bg-base-200 py-8 px-12 rounded-2xl shadow-lg w-lg flex justify-center items-center"
  >
    <div class="w-full">
      <h2 class="text-3xl font-bold text-center mb-8 text-base-content">
        Create your account
      </h2>

      <div v-if="!isLoaded" class="flex justify-center items-center">
        <span class="loading loading-spinner loading-xl"></span>
      </div>
      <div v-else>
        <div v-if="!pendingVerification" class="card bg-base-100 shadow-xl">
          <form @submit.prevent="handleSubmit" class="card-body">
            <div class="form-control">
              <label class="label" for="username">
                <span class="label-text">Username</span>
              </label>
              <input
                id="username"
                v-model="username"
                type="text"
                required
                class="input input-bordered w-full"
              />
            </div>

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
                autocomplete="new-password"
                required
                class="input input-bordered w-full"
              />
            </div>

            <div class="form-control">
              <label class="label" for="role">
                <span class="label-text">Select Role</span>
              </label>
              <select
                id="role"
                v-model="role"
                required
                class="select select-bordered w-full"
              >
                <option
                  v-for="option in roleOptions"
                  :key="option.value"
                  :value="option.value"
                >
                  {{ option.label }}
                </option>
              </select>
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
                {{ loading ? "Signing up..." : "Sign up" }}
              </button>
            </div>

            <div class="text-center mt-4">
              <RouterLink to="/signin" class="text-primary hover:underline">
                Already have an account? Sign in
              </RouterLink>
            </div>
          </form>
        </div>

        <!-- <div v-else class="card bg-base-100 shadow-xl">
          <form @submit.prevent="handleVerifyEmail" class="card-body">
            <div class="form-control">
              <label class="label" for="code">
                <span class="label-text">Verification Code</span>
              </label>
              <input
                id="code"
                v-model="code"
                type="text"
                required
                class="input input-bordered w-full"
              />
              <label class="label">
                <span class="label-text-alt text-base-content/70">
                  Please check your email for a verification code.
                </span>
              </label>
            </div>

            <div v-if="error" class="alert alert-error mt-4">
              {{ error }}
            </div>

            <div class="form-control mt-6">
              <button
                type="submit"
                :disabled="loading"
                class="btn btn-primary"
                :class="{ loading: loading }"
              >
                {{ loading ? "Verifying..." : "Verify Email" }}
              </button>
            </div>
          </form>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useSignUp, useUser } from "@clerk/vue";

const router = useRouter();
const { signUp, isLoaded, setActive } = useSignUp();
const { user } = useUser();

// Form data
const username = ref("");
const emailAddress = ref("");
const password = ref("");
const role = ref("user");
const code = ref("");

// UI state
const pendingVerification = ref(false);
const error = ref("");
const loading = ref(false);

const roleOptions = [
  { value: "user", label: "User" },
  { value: "hr", label: "HR" },
];

const updateUserMetadata = async (userId) => {
  try {
    const response = await fetch(
      `${import.meta.env.VITE_BACKEND_URL}/api/updateMetadata`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: userId,
        }),
      }
    );

    if (!response.ok) {
      throw new Error("Failed to update user metadata");
    }

    // Reload user to get updated metadata
    await user.value.reload();
  } catch (err) {
    console.error("Error updating metadata:", err);
    throw err;
  }
};

const handleSubmit = async () => {
  if (!isLoaded.value) return;

  try {
    loading.value = true;
    error.value = "";

    const res = await signUp.value.create({
      username: username.value,
      emailAddress: emailAddress.value,
      password: password.value,
      unsafeMetadata: {
        role: role.value, // Set temporarily until backend updates it
      },
    });
    console.log("Sign up response:", res);

    if (res.status !== "complete") {
      error.value = `Sign up status: ${res.status}`;
      return;
    }

    await setActive.value({ session: res.createdSessionId });

    try {
      // Update metadata on backend and reload user
      await updateUserMetadata(res.createdUserId);

      // Route based on role
      if (role.value === "hr") {
        router.push("/hr-dashboard");
      } else if (role.value === "user") {
        router.push("/user-dashboard");
      }
    } catch (metadataError) {
      console.error("Error updating metadata:", metadataError);
      error.value = "Failed to set user role. Please contact support.";
    }
  } catch (err) {
    console.error("Error during sign up:", err);
    error.value = err.message || "An error occurred during sign up";
  } finally {
    loading.value = false;
  }
};

// const handleVerifyEmail = async () => {
//   if (!isLoaded.value) return;

//   try {
//     loading.value = true;
//     error.value = "";

//     const completeSignUp = await signUp.value.attemptEmailAddressVerification({
//       code: code.value,
//     });

//     if (completeSignUp.status !== "complete") {
//       error.value = `Sign up status: ${completeSignUp.status}`;
//       return;
//     }

//     await setActive.value({ session: completeSignUp.createdSessionId });
//     router.push("/dashboard");
//   } catch (err) {
//     console.error("Error during verification:", err);
//     error.value = err.message || "An error occurred during verification";
//   } finally {
//     loading.value = false;
//   }
// };
</script>
