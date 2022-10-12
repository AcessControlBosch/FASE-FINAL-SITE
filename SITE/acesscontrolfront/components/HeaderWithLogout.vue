<template>

    <div>

        <div class="supergrafico"></div>

        <div class="row">

            <img src="../static/logo.svg" />

            <button v-on:click="logout()"><i class="pi pi-sign-out"></i></button>

        </div>

    </div>

</template>

<script>
export default {
  name: 'HeaderWithLogout',

    methods: {
        
        logout: async function(){

            await this.$store.dispatch("SET_USER", {});
            this.$auth.logout()

        }

    },

}
</script>

<style lang="scss" scoped>

    @import "@/layouts/_scss_components/HeaderWithHome.scss";

</style>