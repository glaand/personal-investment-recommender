<template>
  <v-app-bar flat>
    <v-app-bar-title>
      <v-icon icon="mdi-circle-slice-6" />

      Personal Investment Recommender
      <!-- logout button, show if is not home -->
      <v-btn v-if="route.path != '/'" :to="'/'">
        <v-icon>mdi-logout</v-icon> Ausloggen
      </v-btn>
    </v-app-bar-title>
  </v-app-bar>
</template>

<script lang="ts" setup>
  import { useRoute } from 'vue-router';
  const route = useRoute();
</script>
