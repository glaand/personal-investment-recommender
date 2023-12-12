<template>
    <v-responsive>
      <h3>
        Dein aktuelles Portfolio 
        <v-chip v-if="beta >= 1" class="ml-1" size="small" variant="flat" color="red">Portfolio Risiko: Hoch (Beta: {{ beta }})</v-chip>
        <v-chip v-else-if="beta < 1" class="ml-1" size="small" variant="flat" color="green">Portfolio Risiko: Tief (Beta: {{ beta }})</v-chip>
      </h3>
      <v-table density="compact" class="mt-2">
        <thead>
          <tr>
            <th class="text-left">Währung</th>
            <th class="text-left">Anzahl</th>
            <th class="text-left">Name</th>
            <th class="text-left">ISIN</th>
            <th class="text-left">Einstand</th>
            <th class="text-left">Marktkurs</th>
            <th class="text-left">Marktwert</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="item in stocks"
            :key="item.name"
          >
            <td>{{ item.currency }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.isin }}</td>
            <td>{{ item.buy_price }}</td>
            <td>{{ item.price }}</td>
            <td>{{ item.value }}</td>
          </tr>
        </tbody>
      </v-table>
    </v-responsive>
  </template>
  
  <script lang="ts" setup>
    import { ref, computed } from 'vue';
    
    const props = defineProps({
      portfolio: {
        type: Object,
        required: true,
      },
      beta: {
        type: Number,
        required: true,
      },
    });

    const stocks = computed(() => {
      return props.portfolio._portfolio;
    });

  </script>
  