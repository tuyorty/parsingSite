<template>
  <v-app>
    <v-main class="gradient-color">
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

<style scoped>
  .gradient-color{
    margin:0px;
    padding:0px;
    font-family:"Helvetica";
    background-image:linear-gradient( 140deg,#2c3e50,#27ae60,#2980b9,#e74c3c,#8e44ad);
    background-size:400%;
    animation:beginani 15s infinite;
  }

  @keyframes beginani{
    0%{
      background-position:0% 50%;
    }
    50%{
      background-position:100% 50%;
    }
    100%{
      background-position:0% 50%;
    }
  }
</style>
