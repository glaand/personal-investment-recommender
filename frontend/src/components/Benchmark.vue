<template>
    <v-responsive>
      <h3>Vergleich mit dem CIO Benchmark Portfolio</h3>
      <v-row>
        <v-col style="height: 500px">
            <Bar
                id="market-allocation"
                :options="options"
                :data="marketAllocationData"
            />
        </v-col>
      </v-row>
      <v-row>
        <v-col style="height: 500px">
            <Bar
                id="sector-allocation"
                :options="options"
                :data="sectorAllocationData"
            />
        </v-col>
      </v-row>
    </v-responsive>
  </template>
  
  <script lang="ts" setup>
    import {
        Chart as ChartJS,
        Title,
        Tooltip,
        Legend,
        BarElement,
        CategoryScale,
        LinearScale
    } from 'chart.js'
    import { Bar } from 'vue-chartjs'
    import ChartDataLabels from 'chartjs-plugin-datalabels';
    import { ref, computed } from 'vue';

    ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, ChartDataLabels);
    
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
        const labels = [
            'Financial Services', 
            'Technology', 
            'Industrials', 
            'Energy', 
            'Healthcare', 
            'Consumer Defensive', 
            'Consumer Cyclical', 
            'Basic Materials', 
            'Real Estate', 
            'Communication Services', 
            'Utilities',
            'Mixed'
        ];
        const marketValues = Object.values(props.sector).map((value) => {
            return parseFloat(value * 100);
        });
        const datasets = [
            {
                label: "Sektor",
                data: marketValues,
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
  