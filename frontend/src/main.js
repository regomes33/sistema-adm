import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


const app = createApp(App)

app.use(router)

app.mount('#app')

// // // Make BootstrapVue available throughout your project
// app.use(BootstrapVue)
// // // Optionally install the BootstrapVue icon components plugin
// app.use(IconsPlugin)



