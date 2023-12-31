<template>
  <v-container v-if="portfolio">
    <h3 class="text-center">Willkommen beim Personal Investment Recommender, {{ portfolio._name }}!</h3>
    <v-tabs
      v-model="tab"
      color="deep-purple-accent-4"
      align-tabs="center"
    >
      <v-tab value="recommendations"><v-icon class="mr-2">mdi-star</v-icon>Empfehlungen</v-tab>
      <v-tab value="portfolio"><v-icon class="mr-2">mdi-book-open-variant</v-icon>Portfolio</v-tab>
      <v-tab value="warnings"><v-icon class="mr-2">mdi-alert</v-icon>Warnungen</v-tab>
      <v-tab value="allocation"><v-icon class="mr-2">mdi-chart-pie</v-icon>Allokation</v-tab>
      <v-tab value="benchmark"><v-icon class="mr-2">mdi-chart-box-outline</v-icon>Vergleich Benchmark</v-tab>
    </v-tabs>

    <v-window v-model="tab" class="mt-2">
      <v-window-item value="recommendations">
        <p class="my-3">Basierend auf deinem Portfolio haben wir einen individuellen Vorschlag für dich vorbereitet.</p>
        <v-responsive class="align-center text-center mt-6">
          <v-row class="pb-2">
            <v-col md="4" cols="12">
              <v-expansion-panels variant="accordion">
                <v-expansion-panel-title hide-actions class="crystal-teal-header">
                  <h3>Something Essential</h3>Diversifikationsstrategien
                </v-expansion-panel-title>
                <Recommendation 
                  v-for="(recommendation, i) in recommendations.something_essential" 
                  type="essential"
                  :key="i"
                  :user="portfolio._name"
                  :recommendation="recommendation"
                  class="crystal-teal-row"
                ></Recommendation>
              </v-expansion-panels>
              <v-card class="pa-2 text-left" variant="tonal" color="indigo">
                Dieser Algorithmus setzt auf bewährte Diversifikationsstrategien. Wir analysieren die Markt- und Sektorallokation deines Portfolios und präsentieren dir Aktien, die deine Allokation sinnvoll ergänzen könnten. Dabei berücksichtigen wir auch deine persönlichen Vorlieben, die du in naher Zukunft direkt hier spezifizieren kannst.
              </v-card>
            </v-col>
            <v-col md="4" cols="12">
              <v-expansion-panels variant="accordion">
                <v-expansion-panel-title hide-actions class="aquamarine-header">
                  <h3>Something Similar α</h3>Branchenverwandtschaft im Fokus</v-expansion-panel-title>
                <Recommendation 
                  v-for="(recommendation, i) in recommendations.something_similar"
                  type="alpha"
                  :key="i" 
                  :user="portfolio._name"
                  :recommendation="recommendation"
                  class="aquamarine-row"
                ></Recommendation>
              </v-expansion-panels>
              <v-card class="pa-2 text-left" variant="tonal" color="green-darken-5">
                Unser intelligenter Textalgorithmus analysiert die Branchenaffinität deiner Aktien. Er identifiziert Schlüsselbegriffe in den Sektoren und Branchen, schlägt dir dann gezielt ähnliche Unternehmen vor. So erhältst du passende Vorschläge basierend auf textuellen Ähnlichkeiten.
              </v-card>
            </v-col>
            <v-col md="4" cols="12">
              <v-expansion-panels variant="accordion">
                <v-expansion-panel-title hide-actions class="caribbean-green-header">
                  <h3>Something Similar β</h3> Modernste Textanalyse für Ähnlichkeiten
                </v-expansion-panel-title>
                <Recommendation 
                  v-for="(recommendation, i) in recommendations.something_special"
                  type="beta"
                  :key="i"
                  :user="portfolio._name"
                  :recommendation="recommendation"
                  class="caribbean-green-row"
                ></Recommendation>
              </v-expansion-panels>
              <v-card class="pa-2 text-left" variant="tonal" color="green-darken-1">
                Dieser innovative Ansatz berücksichtigt deine Anlagepräferenzen, indem er die Schwerpunkte innerhalb deines Portfolios identifiziert. Mithilfe fortschrittlicher Methoden aus dem Bereich des Natural Language Processing werden textuelle Ähnlichkeiten genutzt, um Unternehmen zu finden, die deinen Favoriten ähneln.
              </v-card>
            </v-col>
          </v-row>
          <p>Diese Darstellung dient ausschliesslich zu Demonstrationszwecken und stellt keine Anlageempfehlung dar. Sie sollte nicht als solche interpretiert werden.</p>
        </v-responsive>
      </v-window-item>

      <v-window-item value="portfolio">
        <Portfolio :portfolio="portfolio" :beta="portfolio._portfolio_beta" />
      </v-window-item>

      <v-window-item value="warnings">
        <Warnings
          :sell_stocks="portfolio._sell_stocks" 
          :bulk_stocks="portfolio._bulk_risks" 
          :high_beta_stocks="portfolio._high_beta_stocks"
        />
      </v-window-item>

      <v-window-item value="allocation">
        <Allocation
          :market="portfolio._market_allocation" 
          :sector="portfolio._sector_allocation" 
        />
      </v-window-item>

      <v-window-item value="benchmark">
        <Benchmark
          :market="portfolio._market_allocation_difference" 
          :sector="portfolio._sector_allocation_difference" 
        />
      </v-window-item>
    </v-window>
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

  const tab = ref('recommendations');

   // get url parameter id
    const id = route.params.id;

  onMounted(() => {
    getPortfolio(id);
    getRecommendations(id);
  });
</script>

<style scoped lang="scss">
  .crystal-teal-header {
    background-color: #02647E;
    color: white;
  }
  .crystal-teal-row {
    background-color: lighten(#02647E, 70%);
  }

  .aquamarine-header {
    background-color: #16a587;
    color: white;
  }

  .aquamarine-row {
    background-color: lighten(#16a587, 60%);
  }

  .caribbean-green-header {
    background-color: #00CC9C;
    color: white;
  }

  .caribbean-green-row {
    background-color: lighten(#00CC9C, 50%);
  }

  .v-expansion-panel-title {
    font-size: 11px;
  }

</style>