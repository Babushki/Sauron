import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const rooms = {
  rooms: ['215', '216', '217']
}
const whitelists={
  whitelists: ['C++ Klokwium','Java Kolokwium','Python Zaliczenie']
}
  
const validCredentials = {
  login: 'ppiesiak',
  password: 'dupa'
}

export default new Vuex.Store({
  state: {
    loading: false,
    error: false,
    errorMessage: '',
    errorTimeout: {},
    logged: false,
    rooms: [],
    room: "",
    whitelists: [],
    whitelist: ""
  },
  mutations: {
    LOGIN(state, data) {
      state.logged = data
    },
    ERROR(state, message) {
      state.error = true
      state.errorMessage = message
      clearTimeout(state.errorTimeout)
      state.errorTimeout = setTimeout(() => {
        state.error = false
      }, 5000)
    },
    LOADING(state, data) {
      state.loading = data
    },
    UPDATE_ROOMS(state, rooms) {
      state.rooms = rooms
    },
    CHANGE_ROOM(state, roomName) {
      state.room = roomName
    },
    UPDATE_WHITELISTS(state, whitelists){
      state.whitelists = whitelists
    },
    CHANGE_WHITELIST(state, selectedWhitelist){
      state.whitelist = selectedWhitelist
    }
  },
  actions: {
    login(context, credentials) {
      return new Promise((resolve, reject) => {
        context.commit('LOADING', true)
        context.commit('LOGIN', false)

        // call api to login with credentials.login and credentials.password

        setTimeout(() => {
          if (credentials.login === validCredentials.login && credentials.password === validCredentials.password) {
            window.sessionStorage.setItem('Authorization', 'dawkon1oi2nt')
            context.commit('LOGIN', true)
            resolve()
          } else {
            context.commit('ERROR', "Logowanie nie powiodło się")
            reject()
          }

          context.commit('LOADING', false)
        }, 2500)
      })
    },
    logout(context) {
      window.sessionStorage.removeItem('Authorization')
      context.commit('LOGIN', false)
    },
    fetchRooms(context) {
      return new Promise((resolve, reject) => {
        context.commit('LOADING', true)
        context.commit('UPDATE_ROOMS', rooms.rooms)
        context.commit('LOADING', false)
        resolve()
      })
    },
    chooseRoom(context, roomName) {
      context.commit('CHANGE_ROOM', roomName)
    },
    fetchWhitelists(context){
      return new Promise((resolve,reject) =>{
        context.commit('LOADING', true)
        context.commit('UPDATE_WHITELISTS', whitelists.whitelists)
        context.commit('LOADING', false)
        resolve()
      })
    },
    chooseWhitelist(context, selectedWhitelist){
      context.commit('CHANGE_WHITELIST', selectedWhitelist)
    }
  }
})
