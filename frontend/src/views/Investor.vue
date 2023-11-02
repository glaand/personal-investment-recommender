<template>
  <v-container v-if="portfolio">
    <h3 class="mt-5">Hallo {{ portfolio._name }}!</h3>
    <p class="my-3">Auf Basis deines Portfolios wurden folgende Vorschläge für dich vorbereitet:</p>
    <v-responsive class="align-center text-center mt-6">
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
    <Warnings class="mt-15"
      :sell_stocks="portfolio._sell_stocks" 
      :bulk_stocks="portfolio._bulk_risks" 
    />
    <Portfolio class="mt-15" :portfolio="portfolio" />
    <Allocation class="mt-15"
      :market="portfolio._market_allocation" 
      :sector="portfolio._sector_allocation" 
    />
    <Benchmark class="mt-15"
      :market="portfolio._market_allocation_difference" 
      :sector="portfolio._sector_allocation_difference" 
    />
  </v-container>
  <v-container v-else>
    <h3 class="mt-5">Profile not found...</h3>
  </v-container>
</template>

<script lang="ts" setup>
  import { ref, onMounted } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  import Recommendation from '../components/Recommendation.vue';
  import Portfolio from '../components/Portfolio.vue';
  import Allocation from '../components/Allocation.vue';
  import Benchmark from '../components/Benchmark.vue';
  import Warnings from '../components/Warnings.vue';

  const router = useRouter()
  const route = useRoute()

  const portfolio = ref(null);
  const getPortfolio = async (investor_id) => {
    let uri = process.env.VITE_BACKEND_URL;
    if (uri === undefined) {
      uri = 'http://localhost:8005';
    }
    const response = await fetch(`${uri}/investors/${investor_id}`);
    const data = await response.json();
    portfolio.value = data;
  };

  const recommendations = ref([]);
  const getRecommendations = async (investor_id) => {
    let uri = process.env.VITE_BACKEND_URL;
    if (uri === undefined) {
      uri = 'http://localhost:8005';
    }
    const response = await fetch(`${uri}/recommendations/${investor_id}`);
    const data = await response.json();
    recommendations.value = data;
  };

   // get url parameter id
    const id = route.params.id;

  onMounted(() => {
    getPortfolio(id);
    getRecommendations(id);
  });
</script>
