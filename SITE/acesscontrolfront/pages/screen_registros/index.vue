<template>

    <div class="container">

        <HeaderWithPathHome />

        <div class="row-superior">

            <TitleRegister />

        </div>

        <div class="row-inferior">

            <div class="content-table">

                <div class="index-table">

                    <table class="table-register">

                        <tr class="tr-register">

                            <th class="th-register"><p class="title-table">Name</p></th>
                            <th class="th-register"><p class="title-table">Date</p></th>
                            <th class="th-register"><p class="title-table">Hour Initial</p></th>
                            <th class="th-register"><p class="title-table">Hour Finish</p></th>
                            <th class="th-register"><p class="title-table">Type</p></th>
                            <th class="th-register"><p class="title-table">Exams</p></th>
                            <th class="th-register"><p class="title-table">Result</p></th>

                        </tr>

                        <tr v-for="(register, id) in registerMachine.reverse()" :key="id" class="tr-register">
                           <td class="td-register"><p class="text-table ">{{register.idAssociateFK.name}}</p></td> 
                           <td class="td-register"><p class="text-table text-align-center">{{register.date}}</p></td>
                           <td class="td-register"><p class="text-table text-align-center">{{register.InitialHour}}</p></td>
                           <td class="td-register"><p class="text-table text-align-center">{{register.FinishHour}}</p></td>  
                           <td class="td-register"><p class="text-table text-align-center">{{register.idAssociateFK.jobposition.typeJob}}</p></td>  
                           <td class="td-register"><p class="text-table text-align-center">{{register.examA}} , {{register.examB}}</p></td> 
                           <td class="td-register"><p class="text-table text-align-center">{{register.result}}</p></td>
                        </tr>

                    </table>
                    
                </div>

            </div>

        </div>

    </div>

</template>

<script>

export default{

    name: "screen_registros",

    //GET na API
    created() {

        this.$axios.get(this.$store.state.BASE_URL + "/getreleasemachines/").then((response) => {

            console.log(response)

            this.responseRegisters = response.data;

            let increment = 0;

            for(increment; increment < this.responseRegisters.length; increment++) {


               if(this.responseRegisters[increment].idMachineFK.id.toString() === this.$store.state.idmachine){

                    this.registerMachine.push(this.responseRegisters[increment]);

               }
               
            }

        }).catch((error) => {

            console.log(error)

        });
        
    },

    data(){

        return{
            responseRegisters: [],
            registerMachine:[]
        }

    }

}

</script>

<style lang="scss" scoped>

    @import "@/layouts/_responsividade/responsividade_grid.scss"; 
    @import "@/layouts/_normal_pages/Screen_Registros.scss";

</style>