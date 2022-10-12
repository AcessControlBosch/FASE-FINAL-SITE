<template>
  
  <div class="container">

    <Header />

    <div class="title_page">
        <p class="title_text">Acompanhamento em tempo real</p>
    </div>

    <div class="align-items-center">
    
      <div class="line_legenda">

        <div class="color-on"></div>

        <div class="content_text">
          <div class="text-legenda">Ligada</div>
        </div>

      </div>

      <div class="line_legenda">

        <div class="color-off"></div>
        <div class="content_text">
          <div class="text-legenda">Desligada</div>
        </div>

      </div>
    
    </div>

    <div class="map">

      <div class="line_machines">

        <div v-for="(machine, id) in machines" :key="id" >

            <div v-if="machine.status === false" class="machine_off">

              {{machine.name}}
            
            </div>

            <div v-if="machine.status === true" class="machine_on">

              {{machine.name}}
            
            </div>

        </div>

      </div>


    </div>

  </div>

</template>

<style lang="scss" scoped>

    @import "@/layouts/_scss_normal_pages/screen_index.scss";

</style>

<script>
export default {
  name: 'IndexPage',

  data(){
    return{
      machines:[]
    }
  },

  beforeCreate() {
    
    this.$axios.get(this.$store.state.BASE_URL + "/machines/").then((response) => {

      this.machines = response.data;
      console.log(this.machines)

    })

  },

  mounted(){

    this.verifyMachines();

  },

  methods:{

    verifyMachines: function(){

      setInterval(() => {
        
        this.$axios.get(this.$store.state.BASE_URL + "/machines/").then((response) => {

        this.machines = response.data;
        console.log(this.machines)

        })
        
      }, 5000);

    }

  }

}
</script>