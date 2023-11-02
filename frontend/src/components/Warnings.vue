<template>
  <v-responsive>
    <h3>Warnungen</h3>
    <v-alert
      v-for="sell_stock in sell_stocks"
      :key="sell_stock.isin"
      density="compact"
      type="warning"
      :title="sell_stock.isin"
      :text="sell_stock.name + ': CIO Least Preferred'"
      class="my-2"
      variant="tonal"
    ></v-alert>
    <v-alert
      v-for="bulk_stock in bulk_stocks"
      :key="bulk_stock.isin"
      density="compact"
      type="warning"
      :title="bulk_stock.isin"
      :text="bulk_stock.name + ': Klumpenposition'"
      class="my-2"
    ></v-alert>
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
});
</script>
  