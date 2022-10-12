<template>

    <div class="container">

      <Header />

      <div class="content">

        <div class="row-superior">

            <TitlePage />

        </div>

        <div class="row-inferior">

            <p class="subtitle">VOCÊ JÁ SABE UTILIZAR ESTA INTERFACE?</p>

            <div class="align-items-center">
            
              <button class="btn btn-sucess" v-on:click="$router.push('/screen_qrCode')">SIM</button>
              <button class="btn btn-alert" v-on:click="$router.push('/screen_tutorial')">NÃO</button>
            
            </div>

        </div>
      
      </div>
    
    </div>

</template>


<script>

export default {

  middleware: 'auth',
  name: 'screen_utilizacao',

  beforeCreate() {

    console.log(this.$store.state.usuario)

    if(this.$store.state.usuario.skill === false){
      
      alert("Usuário não tem a permissão para utilizar a máquina!")
      this.$auth.logout()
    
    } else {

      console.log("Tem a permissão")

    }

  },

  data(){

    return{

     responseData: [],
     id: 0

    }

  }

}

</script>

<style lang="scss" scoped>

    @import "@/layouts/_normal_pages/Screen_Utilizacao.scss";
    @import "@/layouts/_responsividade/responsividade_grid.scss";

</style>