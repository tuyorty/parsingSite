<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { Component } from 'vue-property-decorator'
import Vue from 'vue'

@Component({
  components: {

  }
})
export default class App extends Vue {

}
</script>

<style lang="scss" scoped>
</style>
