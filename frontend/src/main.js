import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'

axios.defaults.baseURL='http://127.0.0.1:8000'

const app = createApp(App)

app.use(router)

app.mount('#app')

// // // Make BootstrapVue available throughout your project
// app.use(BootstrapVue)
// // // Optionally install the BootstrapVue icon components plugin
// app.use(IconsPlugin)



