export default {

    SET_USER(context, payload){
        console.log("vuex:" + payload);
        context.commit("USER", payload);
    },

    SET_MACHINE(context, payload){
        console.log("IP_Adress_MACHINE:" + payload);
        context.commit("MACHINE", payload);
    },

    SET_QNOTMARKEDSECURITY(context, payload){
        console.log("qNotMarkedSecurity:" + payload);
        context.commit("QNOTMARKEDSECURITY", payload);
    },

    SET_QNOTMARKEDENVIROMENT(context, payload){
        console.log("qNotMarkedEnviroment:" + payload);
        context.commit("QNOTMARKEDENVIROMENT", payload);
    },

    setipmachine(context, payload){
        console.log("IP_Adress_MACHINE:" + payload);
        context.commit("IPMACHINE", payload);
    },

    setidmachine(context, payload){
        console.log("IDMACHINE:" + payload);
        context.commit("IDMACHINE", payload);
    },

    SET_MODALSECURITY(context, payload){
        console.log("MODAL_SECURITY:" + payload);
        context.commit("MODALSECURITY", payload);
    },

    SET_MODALENVORIMENT(context, payload){
        console.log("MODAL_ENVIROMENT:" + payload);
        context.commit("MODALENVIROMENT", payload);
    },

    SET_ADMIN(context, payload){
        console.log("ADMIN:" + payload);
        context.commit("ADMIN", payload);
    },

    SET_SKILL(context, payload){
        console.log("SKILL:" + payload);
        context.commit("SKILL", payload);
    },

    SET_MACHINE_UPDATE(context, payload){
        console.log("MACHINE_UPDATE:" + payload);
        context.commit("UPDATEMACHINE", payload);
    },

    SET_ID_REALISED(context, payload){
        console.log("IDREALISED:" + payload);
        context.commit("IDREALISED", payload);
    },

    
}