import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Main from './views/Main.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login,
      beforeEnter: (to, from, next) => {
        window.sessionStorage.setItem('Authorization', 'dawkon1oi2nt')
        next()
      }
    },
    {
      path: '/main',
      name: 'main',
      component: Main,
      beforeEnter: (to, from, next) => {
        if (window.sessionStorage.getItem('Authorization')) {
          next()
        } else {
          window.confirm('Brak aktywnej sesji')
          next(false)
        }
      }
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
