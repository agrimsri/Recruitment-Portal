<template class="flex">
  <main class="flex items-center justify-center h-full">
    <!-- <SignIn
      :routing="routing"
      :appearance="{
        elements: {
          rootBox: '!bg-slate-700',
          card: '!bg-slate-700',
          footer: '!bg-slate-700',
          headerTitle: '!text-slate-800 !font-bold !text-2xl',
          headerSubtitle: '!text-slate-600',
          formButtonPrimary:
            '!bg-slate-600 hover:!bg-slate-700 !text-white !font-semibold !py-2 !px-4 !rounded-lg !transition-colors !duration-200',
          formFieldInput:
            '!rounded-lg !border-slate-300 focus:!ring-slate-500 focus:!border-slate-500',
          footerActionLink: '!text-slate-600 hover:!text-slate-800',
          socialButtonsBlockButton:
            '!border !border-slate-300 hover:!bg-slate-50 !transition-colors !duration-200',
          socialButtonsProviderIcon: '!w-5 !h-5',
        },
        variables: {
          colorPrimary: '#475569',
          borderRadius: '0.5rem',
        },
      }"
    /> -->
    <Signup />
  </main>
</template>

<script setup>
import { SignIn } from "@clerk/vue";
import Signup from "@/components/Signup.vue";
import { ref } from "vue";

const routing = {
  afterSignInUrl: "/dashboard",
  afterSignUpUrl: "/dashboard",
};
</script>
