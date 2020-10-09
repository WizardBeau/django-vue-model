// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'babel-polyfill'
import Vue from 'vue'
import App from './App.vue'
import './http'
import router from './router'
import vuetify from '@/plugins/vuetify'
import '@mdi/font/css/materialdesignicons.css'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
