<template>
  <div class="navbar bg-base-100 shadow-sm px-10">
    <div class="navbar-start">
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            fill="none"
            viewBox="0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h8m-8 6h16"
            />
          </svg>
        </div>
        <ul
          tabindex="0"
          class="menu menu-sm dropdown-content bg-base-100 rounded-box z-50 mt-3 w-52 p-2 shadow"
        >
          <SignedIn>
            <li v-if="user?.publicMetadata?.role === 'recruiter'">
              <RouterLink to="/recruiter-dashboard">Dashboard</RouterLink>
            </li>
            <li v-if="user?.publicMetadata?.role === 'candidate'">
              <RouterLink to="/candidate-dashboard">Dashboard</RouterLink>
            </li>
          </SignedIn>
        </ul>
      </div>
      <RouterLink to="/" class="text-xl font-bold">AI Recruiter</RouterLink>
    </div>

    <div class="navbar-center hidden lg:flex">
      <ul class="menu menu-horizontal px-1">
        <SignedIn>
          <li v-if="user?.publicMetadata?.role === 'recruiter'">
            <RouterLink to="/recruiter-dashboard">Dashboard</RouterLink>
          </li>
          <li v-if="user?.publicMetadata?.role === 'candidate'">
            <RouterLink to="/candidate-dashboard">Dashboard</RouterLink>
          </li>
        </SignedIn>
      </ul>
    </div>

    <div class="navbar-end gap-3">
      <SignedOut>
        <ul class="menu menu-horizontal px-1">
          <li>
            <RouterLink to="/signin">Log In</RouterLink>
          </li>
          <li>
            <RouterLink to="/signup">Sign Up</RouterLink>
          </li>
        </ul>
      </SignedOut>

      <SignedIn>
        <UserButton afterSignOutUrl="/" />
      </SignedIn>
    </div>
  </div>
</template>

<script setup>
import { useUser } from "@clerk/vue";
import { SignedIn, SignedOut, UserButton } from "@clerk/vue";

const { user } = useUser();
</script>
