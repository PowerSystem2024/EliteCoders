import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import { OhVueIcon, addIcons } from "oh-vue-icons"
import {
  ViFileTypeJava,
  SiJavascript,
  ViFileTypeReactjs,
  CoMysql,
  SiSpringboot,
  ViFileTypeTypescriptOfficial
} from "oh-vue-icons/icons"

addIcons(
  ViFileTypeJava,
  SiJavascript,
  ViFileTypeReactjs,
  CoMysql,
  SiSpringboot,
  ViFileTypeTypescriptOfficial
)

const app = createApp(App)
app.component("v-icon", OhVueIcon);

app.mount('#app')
