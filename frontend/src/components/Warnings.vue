<template>
  <v-responsive>
    <h3>Warnungen</h3>
    <v-responsive v-if="sell_stocks.length > 0">
    <h4>CIO Least Preferred</h4>
    <v-row class="flex-wrap">
      <v-col v-for="sell_stock in sell_stocks" :key="sell_stock.isin" cols="3">
        <v-alert
          density="compact"
          type="warning"
          class="my-2 text"
          variant="tonal"
        >
          <label class="title">{{ sell_stock.isin }}</label> <br> <label class="text text-no-wrap">{{ sell_stock.name }}</label>
        </v-alert>
      </v-col>
    </v-row>
    </v-responsive>
    <v-responsive v-if="bulk_stocks.length > 0">
    <h4>Klumpenpositionen</h4>
    <v-row class="flex-wrap">
      <v-col v-for="bulk_stock in bulk_stocks" :key="bulk_stock.isin" cols="3">
        <v-alert
          density="compact"
          type="warning"
          class="my-2 text"
        >
          <label class="title">{{ bulk_stock.isin }}</label> <br> <label class="text text-no-wrap">{{ bulk_stock.name }}</label>
        </v-alert>
      </v-col>
    </v-row>
    </v-responsive>
    <v-responsive v-if="high_beta_stocks.length > 0">
    <h4>Hohe Volatilität</h4>
    <v-row class="flex-wrap">
      <v-col v-for="high_beta_stock in high_beta_stocks" :key="high_beta_stock.isin" cols="3">
        <v-alert
          density="compact"
          type="error"
          class="my-2 text"
        >
          <label class="title">{{ high_beta_stock.isin }}</label> <br> <label class="text text-no-wrap">{{ high_beta_stock.name }}</label>
        </v-alert>
      </v-col>
    </v-row>
    </v-responsive>
  </v-responsive>
</template>
  
  <script lang="ts" setup>
import { ref, computed } from "vue";

const props = defineProps({
  sell_stocks: {
    type: Object,
    required: true,
  },
  bulk_stocks: {
    type: Object,
    required: true,
  },
  high_beta_stocks: {
    type: Object,
    required: true,
  },
});
</script>
  
<style scoped lang="scss">

.title {
  font-size: 0.8rem;
}

.text {
  font-size: 0.7rem;
}

</style>