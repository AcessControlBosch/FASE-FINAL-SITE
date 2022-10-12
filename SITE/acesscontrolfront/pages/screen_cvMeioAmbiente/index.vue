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
                        <p class="card-title">Meio Ambiente</p>
                    </div>
                    <div>
                        <p class="card-subject">Requisitos de Meio Ambiente de acordo com o equipamento:​​</p>
                    </div>
                </div>

                <div class="formulario">
                    
                   <div class="line-question" v-for="(question, id) in allQuestions" :key="id">

                        <input type="checkbox" class="checkbox" v-bind:value="idQuestion[id]" v-model="valueCheckBox" v-bind:id="idQuestion[id] - 1"/>
                        <label class="p-question" for="um">{{idQuestion[id]}} - {{question.question}}</label>
                        
                    </div>
                    
                </div>
               
                <div class="align-items-center">
            
                    <button class="btn btn-sucess" v-on:click="verifyQuestions()">Finalizar</button>
                    <button class="btn btn-alert" v-on:click="$router.push('/screen_home')">Cancelar</button>
            
                </div>
                
                <div v-if="showModalEnviroment">
        
                    <ModalOrdemChamadoAmbiente />
        
                </div>

                <div v-if="showModalReleased">

                    <ModalReleased />

                </div>
                
            </div>

        </div>
    
    </div>

</template>

<script>
export default {

    name: 'screen_cvMeioAmbiente',

    data() {

        return {
            intTest: 0,
            allQuestions: [],
            responseQuestions: [],
            valueCheckBox: [],
            idQuestion:[],
            showModalEnviroment: this.$store.state.modalEnviroment,
            path: '',
            showModalReleased: false,
        }

    },

    created(){

        this.path = this.$store.state.BASE_URL + '/greenbooks/' + this.$store.state.idmachine + '/2';

        //console.log(this.path);
         
        this.$axios.get(this.path).then((response) => {

           // console.log('oi created')

            this.allQuestions = response.data;

           // console.log(this.allQuestions)

            let i = 0;

            for(i; i < this.allQuestions.length; i++){

                this.responseQuestions.push(this.allQuestions[i].question);
                this.idQuestion.push(i+1);

            }

           // console.log('this.idQuestion',this.idQuestion)

        }).catch((error) => {

            console.log(error)

        })

    },

    methods:{

        showModalBar: function(){

            this.showModalEnviroment = this.$store.state.modalEnviroment;

        },

        showModalReleasedBar: function(){

            this.showModalReleased = true;

        },

        redirectStandby: function(){
            
            setInterval(() => {
                this.$router.push('/screen_standby');
            }, 3000);
            
        },

        verifyQuestions: function(){

            let qNotMarked  = [];
            let increment = 0;

            for(increment; increment < this.allQuestions.length; increment++){

                var checkedValue = document.getElementById(increment).checked;

                if(checkedValue == false){
                    qNotMarked.push(increment + 1);
                }

            }

            this.$store.dispatch("SET_QNOTMARKEDENVIROMENT", qNotMarked);

            if(this.$store.state.qNotMarkedEnviroment.length > 0){

                this.$store.dispatch("SET_MODALENVORIMENT", true);
                this.showModalBar();
                
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
                let hourFinish = "00:00:00"

                fullHour.toString(); 

                let bodyRealised = [{
                    date: fullDate,
                    InitialHour: fullHour,
                    FinishHour: hourFinish,
                    idMachineFK: this.$store.state.idmachine,
                    idAssociateFK: this.$store.state.usuario.id,
                }]

                let bodyMachine = {
                    name: this.$store.state.machine.name,
                    description: this.$store.state.machine.description,
                    status: true,
                    ipaddress: this.$store.state.machine.ipaddress,
                    statusMaint: this.$store.state.machine.statusMaint
                }
                
                console.log(bodyRealised)
                console.log(bodyMachine)

                this.showModalReleasedBar();
                
                //Post para a API REALISED MACHINES
                this.$axios.post(this.$store.state.BASE_URL + "/releasemachines/", bodyRealised).then((response) => {

                    console.log("Inserção nas maquinas liberadas")
                    
                    let teste = []
                    let idrealesed = 0

                    teste.push(response.data[0])

                    idrealesed = teste[0].id
                    
                    this.$store.dispatch("SET_ID_REALISED", idrealesed);

                }).catch((error) => {
                    console.log(error)
                })

                //Post para a Atualização da máquina
                this.$axios.put(this.$store.state.BASE_URL + "/machines/" + this.$store.state.idmachine + "/", bodyMachine).then(() =>{

                    console.log("Atualização na máquina")

                    this.redirectStandby();

                })
                
            }

        }

    }
}
</script>

<style lang="scss" scoped>
    @import "@/layouts/_normal_pages/Screen_CvMeioAmbiente.scss";
    @import "@/layouts/_responsividade/responsividade_grid.scss";
</style>