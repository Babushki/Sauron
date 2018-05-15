import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loginError: false,
    logged: false
  },
  mutations: {
    LOGIN (state, payload) {
      state.logged = payload
    },
    LOGIN_ERROR (state) {
      state.loginError = true
    }
  },
  actions: {
    login (context, credentials) {
      // call api to login with credentials.login and credentials.password
      console.log(credentials)

      context.commit('LOGIN', true)

      //catch
      //context.commit('LOGIN', false)
      //context.commit('LOGIN_ERROR', true)
    }
  }
})
