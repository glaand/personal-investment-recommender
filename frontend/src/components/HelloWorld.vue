<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-row>
        <v-col>
          <v-expansion-panels variant="accordion">
            <v-expansion-panel-title hide-actions color="orange">Something Similar</v-expansion-panel-title>
            <Recommendation 
              v-for="(recommendation, i) in recommendations.something_similar" 
              :key="i" 
              :recommendation="recommendation"
              color="orange-lighten-3"
            ></Recommendation>
          </v-expansion-panels>
        </v-col>
        <v-col>
          <v-expansion-panels variant="accordion">
            <v-expansion-panel-title hide-actions color="blue">Something Essential</v-expansion-panel-title>
            <Recommendation 
              v-for="(recommendation, i) in recommendations.something_essential" 
              :key="i" 
              :recommendation="recommendation"
              color="blue-lighten-3"
            ></Recommendation>
          </v-expansion-panels>
        </v-col>
        <v-col>
          <v-expansion-panels variant="accordion">
            <v-expansion-panel-title hide-actions color="green">Something Special</v-expansion-panel-title>
            <Recommendation 
              v-for="(recommendation, i) in recommendations.something_special" 
              :key="i" 
              :recommendation="recommendation"
              color="green-lighten-3"
            ></Recommendation>
          </v-expansion-panels>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script lang="ts" setup>
  import { ref, onMounted } from 'vue';
  import Recommendation from './Recommendation.vue';

  const recommendations = ref([]);
  const getRecommendations = async () => {
    let uri = process.env.VITE_BACKEND_URL;
    if (uri === undefined) {
      uri = 'http://localhost:8005';
    }
    const response = await fetch(`${uri}/recommendations/000001`);
    const data = await response.json();
    recommendations.value = data;
  };
  onMounted(getRecommendations);
</script>
