import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

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
    whitelist: "",
    editWhitelist: {},
    students: [],
    student: "",
    oneStudent: {}
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
    UPDATE_WHITELISTS(state, whitelists) {
      state.whitelists = whitelists
    },
    CHANGE_WHITELIST(state, selectedWhitelist) {
      state.whitelist = selectedWhitelist
    },
    EDIT_WHITELIST(state, whitelist) {
      state.editWhitelist = whitelist
    },
    updateEditWhitelistName(state, name) {
      state.editWhitelist.name = name
    },
    updateEditWhitelistAllowed(state, allowed) {
      state.editWhitelist.allowed = allowed
    },
    UPDATE_STUDENTS(state, students) {
      state.students = students
    },
    CHANGE_STUDENT(state, student) {
      state.student = student
    },
    CHANGE_ONE_STUDENT(state, oneStudent){
      state.oneStudent = oneStudent
      console.log(state.oneStudent)
    }
  },
  actions: {
    login(context, credentials) {
      return new Promise((resolve, reject) => {
        context.commit('LOADING', true)
        context.commit('LOGIN', false)

        let authorization = 'Basic ' + window.btoa(`${credentials.login}:${credentials.password}`)
        window.sessionStorage.setItem('Authorization', authorization)

        axios
          .get("http://www.iraminius.pl/sauron/api/auth", {
            headers: {'Authorization': window.sessionStorage.getItem('Authorization')}
          })
          .then(res => {
            context.commit('LOGIN', true)
            context.commit('LOADING', false)
            resolve()
          })
          .catch(() => {
            context.commit('ERROR', 'Nie udało się pobrać listy grup')
            context.commit('LOADING', false)
            reject()
          });
      })
    },
    logout(context) {
      window.sessionStorage.removeItem('Authorization')
      context.commit('LOGIN', false)
    },
    fetchRooms(context) {
      return new Promise((resolve, reject) => {
        context.commit('LOADING', true)        
      })
    },
    chooseRoom(context, roomName) {
      context.commit('CHANGE_ROOM', roomName)
    },
    fetchWhitelists(context) {
      return new Promise((resolve, reject) => {
        context.commit('LOADING', true)

        axios
          .get("http://localhost:3333/whitelists")
          .then(res => {
            context.commit('UPDATE_WHITELISTS', res.data)
            context.commit('LOADING', false)
            resolve()
          })
          .catch(() => {
            context.commit('ERROR', 'Nie udało się pobrać listy grup')
            context.commit('LOADING', false)
            reject()
          });
      })
    },
    chooseWhitelist(context, selectedWhitelist) {
      context.commit('CHANGE_WHITELIST', selectedWhitelist)
    },
    editWhitelist(context, whitelist) {
      context.commit('EDIT_WHITELIST', whitelist)
    },
    deleteWhitelist(context, whitelist) {
      return new Promise((resolve, reject) => {
        context.commit('LOADING', true)
  
        axios
            .delete("http://localhost:3333/whitelists", whitelist.id)
            .then(() => {
              context.dispatch('fetchWhitelists')
            })
            .catch(() => {
              context.commit('ERROR', 'Nie udało się usunąć listy')
              context.commit('LOADING', false)
              reject()
            });
          })
    },
    addWhitelist(context) {
      context.commit('EDIT_WHITELIST', {id: null, name: "Nowa lista", allowed: []})
    },
    saveWhitelist(context) {
      return new Promise((resolve, reject) => {
      context.commit('LOADING', true)

      axios
          .post("http://localhost:3333/whitelists", context.state.editWhitelist)
          .then(() => {
            context.dispatch('fetchWhitelists')
          })
          .catch(() => {
            context.commit('ERROR', 'Nie udało się zapisać listy')
            context.commit('LOADING', false)
            reject()
          });
        })
    },
    fetchStudents(context) {
      return new Promise((resolve, reject) => {
        context.commit('LOADING', true)
        axios
          .get("http://www.iraminius.pl/sauron/api/process", {
            headers: {'Authorization': window.sessionStorage.getItem('Authorization')},
            params:{
              group: this.state.room
            }
          })
          .then(res => {
            context.commit('UPDATE_STUDENTS', res.data)
            context.commit('LOADING', false)
            resolve()
          })
          .catch(() => {
            context.commit('ERROR', 'Nie udało się pobrać listy studentów')
            context.commit('LOADING', false)
            reject()
          });
        context.commit('LOADING', false)
        resolve()
      })
    },
    chooseStudent(context, selectedStudent) {
      return new Promise((resolve, reject) => {
      context.commit('LOADING', true)
      context.commit('CHANGE_STUDENT', selectedStudent)
      axios
          .get("http://www.iraminius.pl/sauron/api/process", {
            headers: {'Authorization': window.sessionStorage.getItem('Authorization')},
            params:{
              nazgul: this.state.student,
              time_from: 0
            }
          })
          .then(res => {
            context.commit('CHANGE_ONE_STUDENT', res.data)
            context.commit('LOADING', false)
            resolve()
          })
          .catch(() => {
            context.commit('ERROR', 'Nie udało się uaktualnić procesów studenta')
            context.commit('LOADING', false)
            reject()
          });
        })
    },
    updateStudents(context){
      setInterval(function(){
        axios
        .get("http://www.iraminius.pl/sauron/api/process", {
          headers: {'Authorization': window.sessionStorage.getItem('Authorization')},
          params:{
            time_from: 0
          }
        })
        .then(res => {
          context.commit('UPDATE_STUDENTS', res.data)
          context.commit('LOADING', false)
          console.log(res.data)
          resolve()
        })
        .catch(() => {
          context.commit('ERROR', 'Nie udało się uaktualnić listy procesów')
          context.commit('LOADING', false)
          reject()
        });
      }, 2000)
      
    }
  }
})
