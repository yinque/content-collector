import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

const app = createApp(App)

// router
import router from "./router";
app.use(router)

// vue-toastification
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
app.use(Toast);

app.mount('#app')
