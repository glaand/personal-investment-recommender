<template>
  <v-expansion-panel>
    <v-expansion-panel-title hide-actions :color="color">{{ recommendation.name }}</v-expansion-panel-title>
    <v-expansion-panel-text>
      <div v-if="recommendationText.length > 0">
        <p><b>Wir empfehlen diese Aktie weil:</b></p>
        <p v-for="msg in recommendationText">{{ msg  }}</p>
        <v-divider class="my-5"></v-divider>
      </div>
      <p><b>Jahresperformance:</b> {{ parseFloat(recommendation["52WeekChange"] * 100).toFixed(2) }}%</p>
      <p><b>P/E:</b> {{ parseFloat(recommendation.trailingPE).toFixed(2) }}</p>
      <p><b>β:</b> {{ parseFloat(recommendation.beta).toFixed(2) }}</p>
      <p><b>Dividende:</b> {{ parseFloat(recommendation.dividend * 100).toFixed(2) }}%</p>
      <v-divider class="my-5"></v-divider>
      <v-row v-if="hasRated == false" align="center" justify="center">
        <v-col cols="auto">
          <v-btn @click="chooseRating('like')" size="x-small" color="success" icon="mdi-check"></v-btn>
        </v-col>
        <v-col cols="auto">
          <v-btn @click="chooseRating('dislike')" size="x-small" color="orange-darken-2" icon="mdi-close"></v-btn>
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
  type: {
    type: String,
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
  user: {
    type: String,
    required: true,
  },
});

const hasRated = ref(false);
const recommendationText = ref([]);

if (props.type == 'essential' || props.type == 'beta') {
  recommendationText.value = props.recommendation.text;
}

const chooseRating = async (action) => {
  hasRated.value = true;
  const ISIN = props.recommendation.isin;
  const type = props.type;
  // get current timestamp
  const timestamp = Date.now();
  const rating = {
    "user": props.user,
    "recommender": type,
    "action": action,
    "stock": ISIN,
    "timestamp": timestamp,
  };
  let uri = process.env.VITE_BACKEND_URL;
  if (uri === undefined) {
    uri = 'http://localhost:8005';
  }
  const response = await fetch(`${uri}/engage`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(rating),
  });
};


</script>