export const state = () => ({

    usuario: {},
    qNotMarkedSecurity: {},
    qNotMarkedEnviroment: {},
    ipAddressMachine: '1',
    idmachine: '1',
    idrealised: '',
    machine: {},
    modalSecurity:  false,
    modalEnviroment:  false,
    admin: false,
    skill: false,

    BASE_URL: "http://localhost:8000",

    coresIniciais: [
        //Cores primários - fortes
        "#219557", //green
        "#001222", //blue
        "#FF2124", //red
        "#FFCF00", //yellow"
        "#B12EA9", //purple
        "#006EAD", //lightblue
        "#147671", //turquiose
        "#007A42", //darkgreen
        "#DEB300", //yellowdark
        "#D50005", //red
        "#003E64", //blue
        "#00884A"//
        
     ],
 
     coresGradient:[
         "#ED0007", //red
         "#9E2896", //purple
         "#007BC0", //blue
         "#18837E", //turquoise
         "#00884A", //green
     ]
    
});