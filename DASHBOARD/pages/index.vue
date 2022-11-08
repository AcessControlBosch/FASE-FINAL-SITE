<template>

  <div class="container">

    <Header />

    <div class="content">

      <div class="options_bar">
        
        <div class="logo-container">

          <img src="../static/logo.svg" />

        </div>

        <div class="menu-container">

          <button class="btn-machine" v-on:click="containerGeral">
            <p class="text-machine-item">Análise Geral</p>
          </button>

          <button class="btn-machine-title">
            <p class="text-machine-item">Máquinas</p>
          </button>
          
          <div v-for="(machine, id) in machines" :key="id">

            <button class="btn-machine-item" v-on:click="mudation(machine)">
              <p class="text-machine-item">{{machine}}</p>
            </button>
                        
          </div>

        </div>

      </div>
      
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
                <p class="text-body">{{this.qtdMachines.length}}</p>
              </div>
            </div>

            <div class="card red">
              <div class="card-title">
                <p class="title">Máquinas em manutenção</p>
              </div>

              <div class="card-body">
                <p class="text-body">{{this.qtdManutencao}}</p>
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
                    <p class="card-grapich-title-text">Comparação entre liberações e manutenções</p>
                </div>

                <div class="container-grapich">

                    <Chart type="bar" :data="lineChartRelease" :options="horizontalOptions"/>

                </div>

              </div>

              

            </div>

            
            </div>


          </div>

          <div v-if="geral === false" class="only-machines">

            <div class="title-machine-name">

              <p class="title-machine-text">Tempo de utilização da máquina por mês</p>

            </div>

            <div class="grapich">

              <Chart type="bar" :data="lineHourPerMonth"/>

            </div>

            <div class="title-machine-name">

              <p class="title-machine-text">Dados gerais</p>

            </div>

            <div class="size-tables">

              <div class="size_one">

                <div class="title-table">
                  <p class="title-table-text">Quantidade de manutenções por mês</p>
                </div>
              
              </div>

              <div class="size_two">

                <div class="title-table">
                  <p class="title-table-text">Quantidade de liberações por mês</p>
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
      qtdMachines: [],
      manuntecoes: [],

      //Dados para a página
      geral: true,
      title: 'Análise gerais sobre as máquinas',  
      day: '',
      month: '',
      year: '',
      qtdManutencao: '',
      nameMachine: '',
      
      //PIECHART -  Utilização por classe
      pieChartReleases: [],
      class: [],
      classQuant: [],

      //BARCHART - Utilização por mês
      barChartMonth: [],
      releaseMonth: [],

      //LINECHART - Comparação entre liberações e manutenções
      lineChartRelease: [],
      horizontalOptions: {
          indexAxis: 'y',
      },

      //BARCHART - Utilização em horas por mês
      lineHourPerMonth: [],
      
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

    }),

    this.$axios.get(this.$store.state.BASE_URL + "/machines/").then((response) => {
      
      this.qtdMachines = response.data;

    }).catch((error) => {

      console.log(error)

    })

  },

  methods: {

    calculateData: function() {

      const date = new Date();
      let increment = 0;
      let verify = false;
      let countQtd = 0;

      this.date = date.getDate();
      this.month = date.getMonth() + 1;
      this.year =  date.getFullYear();

      //--------------------------------------------------
      //QUANTIDADE DE MANUTENÇÕES
      //--------------------------------------------------
      for(increment; increment < this.qtdMachines.length; increment++){

        if(this.qtdMachines[increment].statusMaint === true){
          countQtd = countQtd + 1
        }

      }
      
      this.qtdManutencao = countQtd;

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
          backgroundColor: this.$store.state.coresIniciais,
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
      
      //Preparação dos dados para serem redenizados
      increment = 0;
      let dataSetMonth = []
      
      for(increment; increment < this.machines.length; increment++){

        dataSetMonth.push(
          {
            label: this.machines[increment],
            backgroundColor: this.$store.state.coresIniciais[increment],
            data: [this.releaseMonth[increment]]
          }

        )
        
      }

      let datasetmonthlabel = ['']

      this.barChartMonth = {
        labels: datasetmonthlabel,
        datasets: dataSetMonth
      }

      //--------------------------------------------------
      //LINECHART - Diferença entre Liberação x Manuenções
      //--------------------------------------------------
      increment = 0
      let datasetrelease = []

      let labelRelease = ['Liberações',  'Manutenções']
      let dataRelease = [this.dataMachines.length, this.manuntecoes.length]

      for(increment; increment < 2; increment++){

        datasetrelease.push(
          {
            label: labelRelease[increment],
            backgroundColor: this.$store.state.coresIniciais[increment],
            data: [dataRelease[increment]]
          }
        )
      }

      let datasetreleaselabel = ['']

      this.lineChartRelease = {
        labels: datasetreleaselabel,
        datasets: datasetrelease
      }

    },

    containerGeral: function(){
      this.geral = true;
      this.title = "Análise geral das máquinas"
    },

    mudation: function(nameMachine){

      this.geral = false;
      this.title = "Análise da máquina: " + nameMachine
      this.nameMachine = nameMachine

      let increment = 0;
      let month = 0;
      let monthTime = [0,0,0,0,0,0,0,0,0,0,0,0]
    
      //--------------------------------------------------
      //TEMPO DE UTILIZAÇÃO - Verificar quanto tempo essa máquina foi utilizada por mês
      //--------------------------------------------------
      for(increment; increment < this.dataMachines.length; increment++){

        if(this.dataMachines[increment].idMachineFK.name ===  nameMachine.toString()){

          let data = this.dataMachines[increment].date.split("-").map(e => parseInt(e))

          for(month; month < 13; month++){

            if(data[1] === month){

              let horaInicial = this.dataMachines[increment].InitialHour;
              let horaFinal = this.dataMachines[increment].FinishHour;

              let resultado = this.calcularDiferencaHora(horaInicial, horaFinal)

              let mes = monthTime[month]

              monthTime[month] = mes + resultado

            }

          }

        }

      }

      let labelMonth = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];
      let dataSetMonth = [];
      increment = 0;

      for(increment; increment < 12; increment++){

        dataSetMonth.push(
          {
            label: labelMonth[increment],
            backgroundColor: this.$store.state.coresIniciais[increment],
            data: [monthTime[increment]]
          }
        )

      }

      let datasetmonthlabel = ['']

      this.lineHourPerMonth = {
        labels: datasetmonthlabel,
        datasets: dataSetMonth
      }

      //--------------------------------------------------
      //QUANTIDADE DE MANUTENÇÕES
      //--------------------------------------------------
      month = 0;
      increment = 0

      let qtdMaintence = [0,0,0,0,0,0,0,0,0,0,0,0];

      for(increment; increment < 12; increment++){

        for(month; month < this.observations.length; month++){

          

        }

        
      }

      


    },

    calcularDiferencaHora: function(horaInicialRelease, horaFinalRelease){

      let [horaInicial, minutoInicial, segundoInicial] = horaInicialRelease.split(':').map(hI => parseInt(hI))
      let [horaFinal, minutoFinal, segundoFinal] = horaFinalRelease.split(':').map(hF => parseInt(hF))

      let somaInicial = 0;
      let somaFinal = 0;

      //CONVERSÃO PARA HORA - INICIAL
      if(minutoInicial !== 0){
        minutoInicial = minutoInicial / 60
      }

      if(segundoInicial !== 0){
        segundoInicial = segundoInicial / 3600
      }

      somaInicial = horaInicial + minutoInicial + segundoInicial

      //CONVERSÃO PARA HORA - FINAL
      if(minutoFinal !== 0){
        minutoFinal = minutoFinal / 60
      }

      if(segundoFinal !== 0){
        segundoFinal = segundoFinal / 3600
      }

      somaFinal = horaFinal + minutoFinal + segundoFinal

      let diferenca = 0
      
      if(somaInicial > somaFinal){
        diferenca = somaInicial - somaFinal
      } else {
        diferenca = somaFinal - somaInicial
      }

      return diferenca;

    }

  }

}
</script>
