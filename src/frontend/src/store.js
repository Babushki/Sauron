import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const rooms = {
  rooms: ['215', '216', '217']
}

export default new Vuex.Store({
  state: {
    loading: false,
    error: false,
    errorMessage: '',
    errorTimeout: {},
    logged: false,
    rooms: [],
    room: ""
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
    }
  },
  actions: {
    login(context, credentials) {
      return new Promise((resolve, reject) => {
        context.commit('LOADING', true)
        context.commit('LOGIN', false)

        // call api to login with credentials.login and credentials.password

        setTimeout(() => {
          context.commit('LOGIN', true)
          // context.commit('ERROR', "Logowanie nie powiodło się")

          context.commit('LOADING', false)

          resolve()
          // reject()
        }, 3000)
      })
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
    }
  }
})
