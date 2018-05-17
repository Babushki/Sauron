<template>
      <div class="body-container">
        <div class="students-list">
          <h1> Aktualnie podłączeni użytkownicy do sali {{this.$store.state.room}}</h1>
        
          <table class="table table-striped table-borderes">
            <thead>
              <tr>
                <th>Nazwa:</th>
                <th>Akcja:</th>
              </tr>
            </thead>
            <tbody>
              <tr v-bind:key="student.id" v-for="student in this.$store.state.students">
                <td>{{student.name}}</td>
                <td>
                  <button v-on:click="$store.dispatch('chooseStudent', student)">Podgląd</button>
                  <button v-on:click="$store.dispatch('chooseStudent', student)">Zbanuj</button>
                </td>
              </tr>
            </tbody>
            <br/>
          </table>
        </div>

        <StudentInfo/>
      </div>
</template>

<script>
import axios from "axios";
import StudentInfo from './StudentInfo'

export default {
  name: "Body",
  components: {
    StudentInfo
  },
  mounted() {
    this.$store.dispatch('fetchStudents')
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.body-container {
  display: flex;
  justify-content: space-between;
}
.students-list {
  text-align: center;
  margin-left: 5%;
  height: 100%;
  background-color: lightgray;
  width: 40%;
}
textarea {
  height: 100px;
  width: 200px;
}
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
