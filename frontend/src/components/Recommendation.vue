<template>
  <v-expansion-panel>
    <v-expansion-panel-title hide-actions :color="color">{{ recommendation.name }}</v-expansion-panel-title>
    <v-expansion-panel-text>
      <p>Lorem Ipsum</p>
      <v-row align="center" justify="center" class="mt-5">
        <v-col cols="auto">
          <v-btn size="x-small" color="success" icon="mdi-check"></v-btn>
        </v-col>
        <v-col cols="auto">
          <v-btn size="x-small" color="orange-darken-2" icon="mdi-close"></v-btn>
        </v-col>
      </v-row>
    </v-expansion-panel-text>
  </v-expansion-panel>
</template>

<script lang="ts" setup>
const props = defineProps({
  recommendation: {
    type: Object,
    required: true,
  },
  key: {
    type: Number,
  },
  color: {
    type: String,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
});
</script>