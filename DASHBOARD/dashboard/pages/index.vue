<template>
  <h1>Dashboards</h1>
</template>

<script>

export default {
  name: 'Dashboard',

  data(){

    return{
      dataMachines: [],
      machines: []
    }

  },

  created(){

    this.$axios.get(this.$store.state.BASE_URL + "/getreleasemachines/").then((response) => {

      this.dataMachines = response.data;

      this.calculateData();



    }).catch((error) => {

      console.log(error)

    })

  },

  methods: {
    
    calculateData: function() {
      
      let increment = 0;
      let iMachines = 0;

      this.machines.push(this.dataMachines[0].idMachineFK.name)

      console.log(this.machines[0])

      for(increment; increment < this.dataMachines.length; increment++){




      }
      


    }


  },

}

</script>

<style>


</style>
