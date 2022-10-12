<template>
    <div class="container">

        <HeaderWithLogout />

        <div class="content">

            <div class="row-superior">

                <TitlePage />

            </div>

        <div class="buttons">
            <div class="button-content">
                <button class="button-function" v-on:click="$router.push('/screen_cvSeguranca')">
                    <p class="tipo">Liberar Máquina</p>
                    <i class="pi pi-lock"></i>
                </button>
                <button class="button-function" v-on:click="$router.push('/screen_registros')">
                    <p class="tipo">Registros</p>
                    <i class="pi pi-list" id="pi-reg"><i class="pi pi-pencil" id="pi-list"></i></i>
                </button>
            </div>
    
            </div>
        
        </div>

    </div>
</template>

<script>
export default {

    middleware: 'auth',
    name: 'screen_home',

    data(){
        return{
            ipAddress : '',
        }
    },

    beforeCreate() {
        
        this.$axios.get(this.$store.state.BASE_URL + '/machines/' + this.$store.state.idmachine).then((response) => {

        this.responseMachine = response.data;
        //console.log(this.responseMachine)

        if(this.responseMachine.statusMaint === true){

            alert("Está máquina está em manutenção!")
            this.$auth.logout();
        
        } else {

            this.$store.dispatch("SET_MACHINE_UPDATE", this.responseMachine);
            
        }

      }).catch(error => {
        console.log(error)
      })


    },

    mounted(){
        
       // console.log("IP DA MÁQUINA:" + this.$store.state.idmachine);

         this.$axios.get(this.$store.state.BASE_URL + '/machines/' + this.$store.state.idmachine).then((response) => {
          
            this.ipAddress = response.data.ipaddress;    
            //this.$store.dispatch("setidmachine", this.idMachine);


        }).catch((error) => {
            console.log(error)
        })
    },

    methods: {
        
        teste: function(){
            //console.log(this.$store.state.ipAddressMachine);
            //console.log(this.$store.state.idmachine);
        }


    },

    
    
}
</script>

<style lang="scss" scoped>
    @import "@/layouts/_normal_pages/Screen_Home.scss";
    @import "@/layouts/_responsividade/responsividade_grid.scss";
</style>