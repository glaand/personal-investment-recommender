<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-row>
        <v-col>
          <v-expansion-panels variant="accordion">
            <v-expansion-panel-title hide-actions color="orange">Something Similar</v-expansion-panel-title>
            <v-expansion-panel
              v-for="i in 3"
              :key="i"
              color="orange-lighten-3"
              title="Nvidia"
              text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
            ></v-expansion-panel>
          </v-expansion-panels>
        </v-col>
        <v-col>
          <v-expansion-panels variant="accordion">
            <v-expansion-panel-title hide-actions color="blue">Something Essential</v-expansion-panel-title>
            <v-expansion-panel
              v-for="i in 3"
              :key="i"
              color="blue-lighten-3"
              title="Nestlé"
              text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
            ></v-expansion-panel>
          </v-expansion-panels>
        </v-col>
        <v-col>
          <v-expansion-panels variant="accordion">
            <v-expansion-panel-title hide-actions color="green">Something Special</v-expansion-panel-title>
            <v-expansion-panel
              v-for="i in 3"
              :key="i"
              color="green-lighten-3"
              title="Flughafen Zürich"
              text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
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
  //
</script>
