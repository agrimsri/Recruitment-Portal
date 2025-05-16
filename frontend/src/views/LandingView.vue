<template>
  <div class="min-h-screen">
    <!-- Hero Section -->
    <div class="hero min-h-[80vh] bg-base-200">
      <div class="hero-content flex-col lg:flex-row-reverse gap-8">
        <div class="max-w-lg">
          <img
            src="https://illustrations.popsy.co/amber/hiring-manager.svg"
            alt="AI Recruitment"
            class="w-full h-auto rounded-lg shadow-2xl"
          />
        </div>
        <div class="max-w-lg">
          <h1 class="text-5xl font-bold text-base-content">
            Transform Your Hiring with AI
          </h1>
          <p class="py-6 text-lg text-base-content/80">
            Experience seamless recruitment powered by artificial intelligence.
            From application to hire, our platform streamlines every step with
            intelligent automation and data-driven insights.
          </p>
          <div class="flex gap-4">
            <RouterLink to="/signup" class="btn btn-primary"
              >Get Started</RouterLink
            >
            <a href="#features" class="btn btn-ghost">Learn More</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Features Section -->
    <div id="features" class="py-20 bg-base-100">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl font-bold text-center mb-16 text-base-content">
          Streamline Your Recruitment Process
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="card bg-base-200 shadow-xl">
            <div class="card-body">
              <div class="text-4xl mb-4">👤</div>
              <h3 class="card-title">Smart Registration</h3>
              <p>
                Simplified user onboarding with intelligent profile creation and
                job matching.
              </p>
            </div>
          </div>

          <!-- Feature 2 -->
          <div class="card bg-base-200 shadow-xl">
            <div class="card-body">
              <div class="text-4xl mb-4">🤖</div>
              <h3 class="card-title">AI-Powered Analysis</h3>
              <p>
                Automated processing of resumes, transcripts, and interviews
                using advanced NLP.
              </p>
            </div>
          </div>

          <!-- Feature 3 -->
          <div class="card bg-base-200 shadow-xl">
            <div class="card-body">
              <div class="text-4xl mb-4">📊</div>
              <h3 class="card-title">HR Dashboard</h3>
              <p>
                Comprehensive analytics and tools for efficient candidate
                evaluation and scheduling.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- How It Works Section -->
    <div class="py-20 bg-base-200">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl font-bold text-center mb-16 text-base-content">
          How It Works
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div class="text-center">
            <div class="text-4xl mb-4">1️⃣</div>
            <h3 class="font-bold mb-2">Register</h3>
            <p class="text-base-content/70">
              Create your profile and browse opportunities
            </p>
          </div>

          <div class="text-center">
            <div class="text-4xl mb-4">2️⃣</div>
            <h3 class="font-bold mb-2">Apply</h3>
            <p class="text-base-content/70">Submit applications with ease</p>
          </div>

          <div class="text-center">
            <div class="text-4xl mb-4">3️⃣</div>
            <h3 class="font-bold mb-2">AI Processing</h3>
            <p class="text-base-content/70">
              Automated analysis and enrichment
            </p>
          </div>

          <div class="text-center">
            <div class="text-4xl mb-4">4️⃣</div>
            <h3 class="font-bold mb-2">Interview</h3>
            <p class="text-base-content/70">Schedule and complete interviews</p>
          </div>
        </div>
      </div>
    </div>

    <!-- CTA Section -->
    <div class="py-20 bg-base-100">
      <div class="container mx-auto px-4 text-center">
        <h2 class="text-3xl font-bold mb-6 text-base-content">
          Ready to Transform Your Hiring Process?
        </h2>
        <p class="mb-8 text-lg text-base-content/80 max-w-2xl mx-auto">
          Join thousands of companies using our AI-powered platform to find and
          evaluate the best talent efficiently.
        </p>
        <RouterLink to="/signup" class="btn btn-primary btn-lg">
          Get Started Today
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
// No additional script needed for now
</script>
