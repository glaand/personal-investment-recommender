<template>
  <v-main>
    <router-view v-if="isBackendReachable" />
    <div v-else>
      Loading ...
    </div>
  </v-main>
</template>

<script lang="ts" setup>
  import { ref, onMounted, onBeforeUnmount } from 'vue';
  const isBackendReachable = ref(false);

  const checkInterval = 2000; // Interval in milliseconds to check backend reachability
  let intervalId;

  const checkBackendReachability = async () => {
    let uri = process.env.VITE_BACKEND_URL;
    if (uri === undefined) {
      uri = 'http://localhost:8005';
    }
    try {
      const response = await fetch(`${uri}/`); // Replace with your backend endpoint
      if (response.ok) {
        isBackendReachable.value = true;
      } else {
        isBackendReachable.value = false;
      }
    } catch (error) {
      isBackendReachable.value = false;
    }
  };

  onMounted(() => {
    // Start checking backend reachability periodically
    checkBackendReachability();
    intervalId = setInterval(checkBackendReachability, checkInterval);
  });

  onBeforeUnmount(() => {
    // Clean up the interval when the component is unmounted
    clearInterval(intervalId);
  });

</script>
