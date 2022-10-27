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
      
      this.calculatedData();


    }).catch((error) => {

      console.log(error)

    })

  },

  methods: {

    calculatedData: function(){

      let increment = 0;
      let iMachines = 0;
      var machines = [];
      var lineQuantidade = [["Maquinas", "Quantidade"]];

      const date =  new Date();

      //---------------------------------------------------------------------------------------
      //---------------------------------------------------------------------------------------
      //-----------------------------------Maquinas Utilizadas---------------------------------
      //---------------------------------------------------------------------------------------
      //---------------------------------------------------------------------------------------
      machines.push(this.dataMachines[0].idMachineFK.name);

      for(increment; increment < this.dataMachines.length; increment++){

        let verify = false;

        for(iMachines; iMachines < machines.length; iMachines++){

          if(machines[iMachines] === this.dataMachines[increment].idMachineFK.name){

            verify = true;
            break

          } 

        }

        if(verify === false){

          machines.push(this.dataMachines[increment].idMachineFK.name)

        }

      }

      increment = 0
      iMachines = 0;

      //---------------------------------------------------------------------------------------
      //---------------------------------------------------------------------------------------
      //-----------------------------------Quantidade de liberações----------------------------
      //---------------------------------------------------------------------------------------
      //---------------------------------------------------------------------------------------
      for(increment; increment < this.dataMachines.length; increment++){ 

      
      }
    
      
    },

  }

}

</script>

<style lang="scss" scoped>



</style>