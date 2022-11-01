export default {

  head: {
    title: 'DASHBOARD',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  css: [
      '@/layouts/global.scss',
      'primeflex/primeflex.css',
      '@/layouts/Reset.scss'
  ],

  plugins: [
  ],

  components: true,

  buildModules: [
  ],

  modules: [
    'primevue/nuxt',
    '@nuxtjs/axios',
  ],

  axios: {
    baseURL: '/',
  },

  build: {
    transpile: ['primevue'],
  },

  primevue:{
    theme: "saga-blue",
    ripple: true,
    components:[
      
    ],
  }
}
