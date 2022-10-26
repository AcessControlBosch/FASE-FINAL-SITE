<template>

  <div>

     <!-- <GChart
      type="PieChart"
      :settings="{ packages: ['corechart'] }"
      :data="chartData"
      :options="chartOptions.chart"
      /> -->

  </div>

</template>

<script>

import { GChart } from 'vue-google-charts/legacy'

export default {
  components: {
    GChart
  },

  data(){

    return{

      dataMachines: [],
      machines: []

    }

  },

  created(){

    this.$axios.get(this.$store.state.BASE_URL + "/getreleasemachines/").then((response) => {

      this.dataMachines = response.data;
      console.log(response.data);

      this.calculateData();

    }).catch((error) => {

      console.log(error)

    })


  },

  methods: {

    calculateData: function() {

      //VARIAVEIS DE UTILIZAÇÃO
      let increment = 0;
      let incrementMachines = 0;
      let verifyFindMachines = false;
      let existsMachines = [];

      //QUANTIDADE DE MÁQUINAS CADASTRADAS
      existsMachines.push(this.dataMachines[0].idMachineFK.name)

      for(increment; increment < this.dataMachines.length; increment){

        // for(incrementMachines; incrementMachines < existsMachines.length; incrementMachines){

        //   if(this.dataMachines[increment].idMachineFK.name === existsMachines[incrementMachines]){

        //     break;

        //   } else {

        //     existsMachines.push(this.dataMachines[increment].idMachineFK.name)
        //     break;

        //   }

        // }

      }

      console.log(existsMachines)

    }

  }

}

</script>

<style lang="scss" scoped>



</style>