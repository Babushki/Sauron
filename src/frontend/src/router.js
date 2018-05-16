import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
      beforeEnter: (to, from, next) => {
        if (window.sessionStorage.getItem('Authorization')) {
          next()
        } else {
          window.confirm('Brak aktywnej sesji')
          next(false)
        }
      }
    }
  ]
})
