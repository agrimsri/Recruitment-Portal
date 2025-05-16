<template>
  <div className="navbar bg-base-100 shadow-sm px-10">
    <div className="navbar-start">
      <div className="dropdown">
        <div tabIndex="{0}" role="button" className="btn btn-ghost lg:hidden">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M4 6h16M4 12h8m-8 6h16"
            />
          </svg>
        </div>
        <ul
          tabIndex="{0}"
          className="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow"
        >
          <li><a>Item 1</a></li>
          <li>
            <a>Parent</a>
            <ul className="p-2">
              <li><a>Submenu 1</a></li>
              <li><a>Submenu 2</a></li>
            </ul>
          </li>
          <li><a>Item 3</a></li>
        </ul>
      </div>
      <RouterLink to="/" className="text-xl">H&M</RouterLink>
    </div>
    <div className="navbar-center hidden lg:flex">
      <ul className="menu menu-horizontal px-1">
        <SignedIn>
          <li>
            <RouterLink to="/dashboard">Dashboard</RouterLink>
          </li>
        </SignedIn>
      </ul>
    </div>
    <div className="navbar-end">
      <!-- <SignedOut>
        <SignInButton class="cursor-pointer" />
      </SignedOut> -->
      <SignedOut><RouterLink to="/signup">Register</RouterLink></SignedOut>

      <SignedIn>
        <UserButton />
      </SignedIn>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from "@/stores/auth";
import { SignedIn, SignedOut, SignInButton, UserButton } from "@clerk/vue";
const authStore = useAuthStore();
</script>
