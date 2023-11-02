<template>
  <v-expansion-panel>
    <v-expansion-panel-title hide-actions :color="color">{{ recommendation.name }}</v-expansion-panel-title>
    <v-expansion-panel-text>
      <p>Lorem Ipsum</p>
      <v-divider class="my-5"></v-divider>
      <p><b>YTD:</b> 8.5%</p>
      <p><b>P/E:</b> 8.5%</p>
      <p><b>β:</b> -1.05</p>
      <p><b>Dividends:</b> 12 CHF</p>
      <v-divider class="my-5"></v-divider>
      <v-row v-if="hasRated == false" align="center" justify="center">
        <v-col cols="auto">
          <v-btn @click="hasRated = true" size="x-small" color="success" icon="mdi-check"></v-btn>
        </v-col>
        <v-col cols="auto">
          <v-btn @click="hasRated = true" size="x-small" color="orange-darken-2" icon="mdi-close"></v-btn>
        </v-col>
      </v-row>
      <p v-else>
        Deine Auswahl wurde gespeichert.
      </p>
    </v-expansion-panel-text>
  </v-expansion-panel>
</template>

<script lang="ts" setup>
import {ref,computed} from "vue";

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

const hasRated = ref(false);


</script>