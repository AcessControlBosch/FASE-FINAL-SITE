<template>

    <div class="container">

        <Header/>

        <div class="view-center">

            <p class="text-info">A máquina em utilização. A liberação foi feita com sucesso, bom trabalho! </p>

            <button class="btn_off">
                <p class="text-btn-off" v-on:click="turnOffMachine()">Desligar</p>
            </button>

        </div>

    </div>

</template>

<script>

    export default{

        name: "screen_standby",

        data(){

            return{
                dataMachine: [],
            }

        },

        beforeCreate(){

            this.$axios.get(this.$store.state.BASE_URL + "/releasemachines/" + this.$store.state.idrealised).then((response) => {

                this.dataMachine = response.data
                console.log(this.dataMachine)

            }).catch((error) =>{

                console.log(error)

            })


        },

        methods:{

            updateMachinesFields: function(){

                const date = new Date();
                let bodyMachine = [];

                let hour = date.getHours();          
                let min = date.getMinutes();        
                let seg = date.getSeconds();

                let fullHour = hour + ":" + min + ":" + seg;

                fullHour.toString(); 

                let bodyUpdate = {
                    date: this.dataMachine.date,
                    hour: this.dataMachine.hour,
                    hourFinish: fullHour,
                    id: this.dataMachine.id,
                    idAssociateFK: this.$store.state.usuario.id,
                    idMachineFK: this.$store.state.machine.id
                }

                console.log(bodyUpdate)

                //Atualização na hora em que a máquina foi desligada
                this.$axios.put(this.$store.state.BASE_URL + "/releasemachines/" + this.$store.state.idrealised + "/", bodyUpdate).then((response) => {

                    console.log("Ai caliquinha, deu bom!")
                    this.$router.push("/screen_home")

                })


            },

            turnOffMachine: function(){

                let bodyMachine = {
                    name: this.$store.state.machine.name,
                    description: this.$store.state.machine.description,
                    status: false,
                    ipaddress: this.$store.state.machine.ipaddress,
                    statusMaint: this.$store.state.machine.statusMaint
                }
                
                console.log(bodyMachine);
                
                //Atualização para desligar a máquina
                this.$axios.put(this.$store.state.BASE_URL + "/machines/" + this.$store.state.idmachine + "/", bodyMachine).then((response) => {

                    console.log("Atualização ná maquina");
                    this.updateMachinesFields();

                }).catch((error) => {
                    console.log(error)
                })

            },

        }

    }

</script>

<style lang="scss" scoped>

    @import "@/layouts/_normal_pages/Screen_Standby.scss";
    @import "@/layouts/_responsividade/responsividade_grid.scss";

</style>