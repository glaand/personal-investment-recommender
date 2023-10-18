<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-row>
        <v-col>
          <v-expansion-panels variant="accordion">
            <v-expansion-panel-title hide-actions color="orange">Something Similar</v-expansion-panel-title>
            <v-expansion-panel
              v-for="(recommendation, i) in recommendations.something_similar"
              :key="i"
              color="orange-lighten-3"
              :title="recommendation.name"
              :text="recommendation.description"
            ></v-expansion-panel>
          </v-expansion-panels>
        </v-col>
        <v-col>
          <v-expansion-panels variant="accordion">
            <v-expansion-panel-title hide-actions color="blue">Something Essential</v-expansion-panel-title>
            <v-expansion-panel
              v-for="(recommendation, i) in recommendations.something_essential"
              :key="i"
              color="blue-lighten-3"
              :title="recommendation.name"
              :text="recommendation.description"
            ></v-expansion-panel>
          </v-expansion-panels>
        </v-col>
        <v-col>
          <v-expansion-panels variant="accordion">
            <v-expansion-panel-title hide-actions color="green">Something Special</v-expansion-panel-title>
            <v-expansion-panel
              v-for="(recommendation, i) in recommendations.something_special"
              :key="i"
              color="green-lighten-3"
              :title="recommendation.name"
              :text="recommendation.description"
            ></v-expansion-panel>
          </v-expansion-panels>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
          <v-col cols="auto">
            <v-btn color="primary" prepend-icon="mdi-face-agent">Mit Berater absprechen</v-btn>
          </v-col>
          <v-col cols="auto">
            <v-btn color="primary" variant="outlined" prepend-icon="mdi-close">Schlechte empfehlungen...</v-btn>
          </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script lang="ts" setup>
  import { ref, onMounted } from 'vue';
  const recommendations = ref([]);
  const getRecommendations = async () => {
    const response = await fetch('http://10.96.66.99:8005/recommendations/000001');
    const data = await response.json();
    recommendations.value = data;
  };
  onMounted(getRecommendations);
</script>
