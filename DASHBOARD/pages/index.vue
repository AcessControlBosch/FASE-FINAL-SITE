<template>

  <div class="container">

    <Header />

    <div class="content">

      <div class="options_bar"></div>
      
      <div class="view_data">

        <div class="row_date">

          <p>{{this.title}}</p>
          <p>{{this.date}} / {{this.month}} / {{this.year}}</p>

        </div>

        <div class="data_geral" v-if="geral">

          <div class="line-inital-data">

            <div class="card green">
              <div class="card-title">
                <p class="title">Liberações Realizadas</p>
              </div>

              <div class="card-body">
                <p class="text-body">{{this.dataMachines.length}}</p>
              </div>
            </div>

            <div class="card yellow">
              <div class="card-title">
                <p class="title">Ordens de manutenção</p>
              </div>

              <div class="card-body">
                <p class="text-body">{{this.manuntecoes.length}}</p>
              </div>
            </div>

            <div class="card blue">
              <div class="card-title">
                <p class="title">Quantidade de máquinas</p>
              </div>

              <div class="card-body">
                <p class="text-body">{{this.machines.length}}</p>
              </div>
            </div>

            <div class="card red">
              <div class="card-title">
                <p class="title">Máquinas quebradas</p>
              </div>

              <div class="card-body">
                <p class="text-body">0</p>
              </div>
            </div>

          </div>

          

        </div>
      
      </div>

    </div>

  </div>


</template>

<style lang="scss" scoped>

  @import "@/layouts/_normal_pages/Index.scss";

</style>

<script>

import Chart from 'primevue/chart';

export default {

  components: {
    Chart,
  },

	data() {
		
    return {

      //Dados para análise das máquinas
      dataMachines: [],
      machines: [],
      liberacoes: [],
      manuntecoes: [],

      //Dados para a página
      geral: true,
      title: 'Análise gerais sobre as máquinas',  
      day: '',
      month: '',
      year: '',
      
      //Dados para criação dos graficos
      lineDataLiberacoes: [],

      
		}

	},

  created(){

    this.$axios.get(this.$store.state.BASE_URL + "/getreleasemachines/").then((response) => {
      
      this.dataMachines = response.data;
      console.log(this.dataMachines)

      this.calculateData();

    }).catch((error) => {

      console.log(error)

    }),

    this.$axios.get(this.$store.state.BASE_URL + "/observations/").then((response) => {
      
      this.manuntecoes = response.data;

    }).catch((error) => {

      console.log(error)

    })

  },

  methods: {

    calculateData: function() {

      const date = new Date();

      this.date = date.getDate();
      this.month = date.getMonth() + 1;
      this.year =  date.getFullYear();
      
      //------------------------------------------------
      //Definição da máquinas que estão sendo utilizadas
      //------------------------------------------------
      let increment = 0;
      let iMachines = 0;
      let verify = false;

      this.machines.push(this.dataMachines[0].idMachineFK.name)

      for(increment; increment < this.dataMachines.length; increment++){

        verify = false;

        for(iMachines; iMachines < this.machines.length; iMachines++){

          if(this.machines[iMachines] === this.dataMachines[increment].idMachineFK.name){

            verify = true;
            break;

          }

        }

        if(verify === false){

          this.machines.push(this.dataMachines[increment].idMachineFK.name)

        }

        iMachines = 0

      }

      //--------------------------------------------------
      //Quantidade de vezes em que a máquina foi utilizada
      //--------------------------------------------------
      let count = 0;

      increment = 0;
      iMachines = 0;

      for(iMachines; iMachines < this.machines.length; iMachines++){

        increment = 0;

        for(increment; increment < this.dataMachines.length; increment++){

          if(this.machines[iMachines] === this.dataMachines[increment].idMachineFK.name){

            count = count + 1;

          }
          
        }

        this.liberacoes.push(count)
        count = 0
    
      }

      console.log(this.machines)
      console.log(this.liberacoes)

      increment = 0;
      let dataSetLiberacao = []
      
      for(increment; increment < this.machines.length; increment++){

        dataSetLiberacao.push(
          {
            label: this.machines[increment],
            backgroundColor: this.$store.state.cores[increment],
            data: [this.liberacoes[increment]]
          }

        )
        
      }

      let datasetmachines = ['Liberações por máquinas']

      this.lineDataLiberacoes = {
        labels: datasetmachines,
        datasets: dataSetLiberacao
      }
  
    }

  }



}
</script>
