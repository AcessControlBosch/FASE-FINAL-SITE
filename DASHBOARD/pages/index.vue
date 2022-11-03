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

          <div class="content-grapichs">

            <div class="left-grapichs">

              <div class="card-grapich">

                <div class="card-grapich-content-title">
                    <p class="card-grapich-title-text">Utilização por classe</p>
                </div>

                <div class="container-grapich">

                  <Chart type="pie" :data="pieChartReleases"/>

                </div>

              </div>

            </div>

            <div class="right-grapichs">
            
              <div class="card-grapich">

                <div class="card-grapich-content-title">
                    <p class="card-grapich-title-text">Máquinas mais utilizadas no mes n° {{this.month}}</p>
                </div>

                <div class="container-grapich">

                    <Chart type="bar" :data="barChartMonth" />

                </div>

              </div>

              <div class="card-grapich">

                <div class="card-grapich-content-title">
                    <p class="card-grapich-title-text">Vamo ver o que sai daqui</p>
                </div>

                <div class="container-grapich">

                </div>

              </div>

              

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
      manuntecoes: [],

      //Dados para a página
      geral: true,
      title: 'Análise gerais sobre as máquinas',  
      day: '',
      month: '',
      year: '',
      
      //PIECHART -  Utilização por classe
      pieChartReleases: [],
      class: [],
      classQuant: [],

      //BARCHART - Utilização por mês
      barChartMonth: [],
      releaseMonth: []
      
		}

	},

  created(){

    this.$axios.get(this.$store.state.BASE_URL + "/getreleasemachines/").then((response) => {
      
      this.dataMachines = response.data;

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
      let increment = 0;
      let verify = false;

      this.date = date.getDate();
      this.month = date.getMonth() + 1;
      this.year =  date.getFullYear();

      //--------------------------------------------------
      //PIECHART - Utilização por classe
      //--------------------------------------------------
      let iClasses = 0;

      this.class.push(this.dataMachines[0].idAssociateFK.jobposition.typeJob)

      for(increment; increment < this.dataMachines.length; increment++){

        verify = false;

        for(iClasses; iClasses < this.class.length; iClasses++){

          if(this.class[iClasses] === this.dataMachines[increment].idAssociateFK.jobposition.typeJob){
            verify = true;
            break;
          }

        }

        if(verify === false){
          this.class.push(this.dataMachines[increment].idAssociateFK.jobposition.typeJob)
        }

        iClasses = 0

      }

      //Quantas vezes foi utilizada por classe
      let count = 0;
      increment = 0;
      iClasses = 0;

      for(iClasses; iClasses < this.class.length; iClasses++){

        increment = 0;

        for(increment; increment < this.dataMachines.length; increment++){

          if(this.class[iClasses] === this.dataMachines[increment].idAssociateFK.jobposition.typeJob){
            count = count + 1;
          }
          
        }

        this.classQuant.push(count)
        count = 0
    
      }

      //Configuração de dados para o PIECHART
      let dataSetClass = []

      let datasetmachines = ['Liberações por classe']

      this.pieChartReleases = {
        labels: this.class,
        datasets: [{
          data: this.classQuant,
          backgroundColor: this.$store.state.cores,
        }]
      }

      //--------------------------------------------------
      //BARCHART - Utilização por mês
      //--------------------------------------------------
      increment = 0;
      verify = false;
      let iMachines = 0;

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

      //Definição pelo mês atual
      increment = 0;
      iMachines = 0;
      count = 0;
      let releaseMonth = []

      for(iMachines; iMachines < this.machines.length; iMachines++){

        increment = 0;

        for(increment; increment < this.dataMachines.length; increment++){

          let data = this.dataMachines[increment].date.split("-")

          if(this.machines[iMachines] === this.dataMachines[increment].idMachineFK.name){

            if(data[1] === this.month.toString()){
              count = count + 1;
            }

          }
          
        }

        this.releaseMonth.push(count)
        count = 0
    
      }
      
      //PReparação dos dados para serem redenizados
      increment = 0;
      let dataSetMonth = []
      
      for(increment; increment < this.machines.length; increment++){

        dataSetMonth.push(
          {
            label: this.machines[increment],
            backgroundColor: this.$store.state.cores[increment],
            data: [this.releaseMonth[increment]]
          }

        )
        
      }

      let datasetmonthlabel = ['']

      this.barChartMonth = {
        labels: datasetmonthlabel,
        datasets: dataSetMonth
      }

    }

  }

}
</script>
