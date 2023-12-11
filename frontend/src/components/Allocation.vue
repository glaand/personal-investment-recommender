<template>
    <v-responsive>
      <h3>Deine Allokation</h3>
      <v-row>
        <v-col>
            <Pie
                id="market-allocation"
                :options="options"
                :data="marketAllocationData"
            />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
            <Pie
                id="sector-allocation"
                :options="options"
                :data="sectorAllocationData"
            />
        </v-col>
      </v-row>
    </v-responsive>
  </template>
  
  <script lang="ts" setup>
    import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
    import ChartDataLabels from 'chartjs-plugin-datalabels';
    import { Pie } from 'vue-chartjs'
    import { ref, computed } from 'vue';

    ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels);
    
    const props = defineProps({
      market: {
        type: Object,
        required: true,
      },
      sector: {
        type: Object,
        required: true,
      },
    });

    const options = {
        responsive: true,
        maintainAspectRatio: false,
        aspectRatio: 0.75,
        plugins: {
            datalabels: {
                formatter: (value, ctx) => {
                    let percentage = value.toFixed(2) + "%";
                    return percentage;
                },
                color: '#000',
            }
        }
    }

    const marketAllocationData = computed(() => {
        const labels = ["United States", "Europe", "Switzerland", "Asia & EM"];
        // get market values with the same order as labels
        let marketValues = labels.map((label) => {
            return props.market[label];
        });
        marketValues = marketValues.map((value) => {
            return parseFloat(value * 100);
        });
        const datasets = [
            {
                label: "Markt",
                data: marketValues,
                backgroundColor: [
                    "green",
                    "royalblue",
                    "red",
                    "pink"
                ]
            }
        ];
        return {
            labels,
            datasets
        };    
    });

    const sectorAllocationData = computed(() => {
        const labels = Object.keys(props.sector);
        const sectorValues = Object.values(props.sector).map((value) => {
            return parseFloat(value * 100);
        });
        const datasets = [
            {
                label: "Sektor",
                data: sectorValues,
                backgroundColor: [
                    'lightblue', 
                    'silver', 
                    'steelblue', 
                    'orange', 
                    'lightgreen', 
                    'tan', 
                    'mediumpurple', 
                    'saddlebrown', 
                    'maroon', 
                    'gold', 
                    'teal',
                    'dimgrey'
                ]
            }
        ];
        return {
            labels,
            datasets
        };    
    });

  </script>
  