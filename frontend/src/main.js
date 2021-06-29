import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import router from './router/index.js'
import 'bootstrap'

const app = createApp(App)

app.use(router)

app.mount('#app')
