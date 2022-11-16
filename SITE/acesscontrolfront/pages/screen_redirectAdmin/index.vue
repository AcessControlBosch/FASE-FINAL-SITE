<template>

    <div class="container">
    
        <HeaderWithLogout />

        <div class="buttons">

            <div class="button-content">

                <button class="button-function" v-on:click="$router.push('/screen_dashboard')">
                    <p class="tipo">Dashboards</p>
                    <i class="pi pi-chart-bar" id="pi-dash"></i>
                </button>

                <button class="button-function" v-on:click="$router.push('/screen_realtime')">
                    <p class="tipo">Acompanhamento em tempo real</p>
                    <i class="pi pi-clock" id="pi-real"></i>
                </button>

            </div>

            <div class="button-content">

                <button class="button-function">
                    <p class="tipo">Cadastros</p>
                    <i class="pi pi-pencil" id="pi-register"></i>
                </button>

                <button class="button-function">
                    <p class="tipo">Visualizar Registros</p>
                    <i class="pi pi-folder" id="pi-data"></i>
                </button>

            </div>
        
        </div>

    </div>
    

</template>

<script>

    export default{

        name: 'Screen_redirectAdmin',

    }


</script>

<style lang="scss" scoped>

    @import "@/layouts/_normal_pages/Screen_RedirectAdmin.scss";
    @import "@/layouts/_responsividade/responsividade_grid.scss";

</style>