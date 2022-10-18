<template>
    
    <div class="container">

        <Header />

        <div class="content">

            <div class="row-superior">

                <TitlePage />

            </div>

            <div class="row-inferior">
            
                <div class="card-info">
                    <div>
                        <p class="card-title">Abertura de Ordem de Manutenção</p>
                    </div>
                </div>

                <div class="conteudo">
                    <p>Descreva abaixo a inconformidade encontrada:</p>

                    <Textarea :autoResize="true" rows="15" cols="10" v-model="observation"/>
                </div>

                <div class="align-items-center">
            
                        <button class="btn btn-sucess" v-on:click="sendObservation()">Enviar</button>

                        <div v-if="showDialogV" >
                            <ModalLock/>
                        </div>
            
                    </div>  
            </div>
            
        </div>
    
    </div>

</template>

<script>
export default {
    name: 'screen_ordemManutencao',
    data(){
        return {
            showDialogV: false,
            observation: ''
        }
    },
    methods:{

        showModal(){
            
            this.showDialogV = true;

            setTimeout(() => {
                this.$auth.logout();
            }, 5000);

        },

        sendObservation: function(){

            if(this.observation === ''){

                alert("Atenção, insira a observação!")

            } else {

                const date = new Date();

                let day = date.getDate();
                let month = date.getMonth() + 1;
                let year = date.getFullYear();

                let fullDate = year + "-" + month + "-" + day;

                let hour = date.getHours();          
                let min = date.getMinutes();        
                let seg = date.getSeconds();

                let fullHour = hour + ":" + min + ":" + seg;

                fullHour.toString(); 

                let bodyObservation = [{
                    idMachineFK: this.$store.state.idmachine,
                    idAssociateFK: this.$store.state.usuario.id,
                    date: fullDate,
                    hour: fullHour, 
                    description: this.observation
                }]

                let bodyMachine = {
                    name: this.$store.state.machine.name,
                    description: this.$store.state.machine.description,
                    status: false,
                    ipaddress: this.$store.state.machine.ipaddress,
                    statusMaint: true
                }

                this.$axios.post(this.$store.state.BASE_URL + "/observations/", bodyObservation).then((response) => {
                    
                    console.log(response)
                    this.showModal()

                }).catch((error) => {
                    console.log(error)
                })

                this.$axios.put(this.$store.state.BASE_URL + "/machines/" + this.$store.state.idmachine + "/", bodyMachine).then(() =>{

                    console.log("Atualização na máquina")

                })

            }

        }

    }
}
</script>

<style lang="scss" scoped>
    @import "@/layouts/_normal_pages/Screen_OrdemManut.scss";
    @import "@/layouts/_responsividade/responsividade_grid.scss";
</style>