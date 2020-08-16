import axios from 'axios'
import VueAxios from 'vue-axios'
import Vue from 'vue'

axios.defaults.baseURL = 'http://localhost:8000'

Vue.use(VueAxios, axios)
