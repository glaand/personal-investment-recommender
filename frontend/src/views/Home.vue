<template>
    <v-container class="fill-height">
      <v-responsive>
        <h3>Bitte logge dich ein, um die App zu nutzen.</h3>
        <v-select label="User" :items="items" item-title="name" @update:modelValue="login">
          <template v-slot:item="{ props, item }">
            <v-list-item v-bind="props" :subtitle="item.raw.investor_type"></v-list-item>
          </template>
        </v-select>
      </v-responsive>
    </v-container>
</template>

<script lang="ts" setup>
  import { ref } from 'vue';
  import { useRouter, useRoute } from 'vue-router';

  const router = useRouter()
  const route = useRoute()

  const items = ref([
    { id: '000001', name: 'Lenny Linux - 000001', investor_type: 'swiss-bias' },
    { id: '000002', name: 'Benny Banker - 000002', investor_type: 'swiss-global' },
    { id: '000003', name: 'Louise Vuitton - 000003', investor_type: 'global' },
    { id: '000004', name: 'Robby Robotic - 000004', investor_type: 'swiss-bias' },
    { id: '000005', name: 'Freddy Ferrari - 000005', investor_type: 'swiss-global' },
    { id: '000006', name: 'Ricky Risk - 000006', investor_type: 'global' },
  ]);

  const login = (e: any) => {
    // get item by name
    const item = items.value.find((item) => item.name === e)
    console.log(item);
    router.push({
      name: 'Investor',
      params: { id: item.id }
    })
  }

</script>
