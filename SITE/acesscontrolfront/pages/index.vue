<template>

  <div class="container">

    <Header />

    <div class="content">

        <div class="formulario">

          <TitlePage />

          <label for="edv" class="label-form">EDV:</label>
          <input type="text" placeholder="Digite o EDV..." id="edv" class="input-form" v-model="user.username"/>

          <label for="senha" class="label-form">Senha:</label>
          <input type="password" placeholder="Digite a senha..." id="senha" class="input-form" v-model="user.password"/>


          <div class="align-items-center">

            <button class="btn-logar" v-on:click="makeLogin()">Logar</button>

          </div>

          <div class="align-items-center">

            <button class="btn-redirect" v-on:click="$router.push('/screen_criarConta')">Não possue conta? Clique aqui</button>

          </div>
        
        </div>
    
    </div>

  </div>

</template>

<script>

export default {
  
  name: 'IndexPage',

  data(){

    return{

      dataUser: [],
      user:{
        username: '',
        password: '',
      }

    }

  },

  beforeCreate(){

    this.$axios.get(this.$store.state.BASE_URL + "/associates").then((response) =>{

      this.dataUser = response.data;
      //console.log(this.dataUser)

    }).catch((response) => {
      console.log(response)
    })

  },

  methods: {

    setUser: async function(){

      console.log(this.user.username)

      let increment = 0;

      for(increment; increment < this.dataUser.length; increment++){

        console.log(this.dataUser[increment].EDV)

        if(this.dataUser[increment].EDV === this.user.username){
          
          await this.$store.dispatch("SET_USER", this.dataUser[increment])

        }

      } 

    },

    //FUNÇÃO QUE REALIZA O LOGIN
    makeLogin: async function(){

      if(this.user.username && this.user.password){

        this.$auth.loginWith("local", {data: this.user}).then((response) => {

          this.setUser();

          console.log("Usuário Logado")

        }).catch((response) =>{

          console.log(response)
          alert("Login Incorreto!")

        })

      } else {
        alert("Preencha todos os campos")
      }
    }
  },

}

</script>

<style lang="scss" scoped>

   @import "@/layouts/_normal_pages/Index.scss";
   @import "@/layouts/_responsividade/responsividade_formularios.scss";

</style>
