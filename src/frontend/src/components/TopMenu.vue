<template>
<div>
  <ul>
      <li>
          <router-link to="/home">Podlgąd sali</router-link>
      </li>
  <li class="dropdown">
    <a class="dropbtn" v-if="this.$store.state.whitelist !== ''">Wybrany filtr: {{this.$store.state.whitelist.name}}</a>
    <a v-else> Brak wybranego filtru</a>
    <div class="dropdown-content">
      <a v-for="(data,index) in this.$store.state.whitelists" :key='index'>
          <a v-on:click="submitWhitelist(data)">{{data.name}}</a>
      </a>
      <a><router-link to="/filters">Zarządzaj filtrami</router-link></a>
    </div>
  </li>
  <li class="dropdown">
   <a  v-if="this.$store.state.room !== ''" class="dropbtn">Wybrana sala: {{this.$store.state.room}}</a>
    <a v-else>Brak wybranej sali</a>
    <div class="dropdown-content">
      <a><input  v-model="selected" ></a>
      <a class="btn" type="submit" v-on:click="submitRoom(selected)" > Wejdź do sali</a>
    </div>
  </li>
  <li style="float:right">
    <a v-on:click="logout">
        Wyloguj
    </a>
  </li>
  
</ul>
</div>
</template>

<script>
import Link from 'vue-router'

export default {
        name: 'TopMenu',
        data () {
            return {
                selected: ""
            }
        },
        mounted() {
             this.$store.dispatch('fetchWhitelists');
        },
        methods: {
            logout() {
                this.$store.dispatch('logout').then(() => {
                    this.$router.push('/')
                })
            },
            submitRoom: function(){
            this.$store.dispatch("chooseRoom", this.selected);
            this.$store.dispatch("fetchStudents");
            },
            submitWhitelist: function(whitelist){
            this.$store.dispatch("chooseWhitelist", whitelist)
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}

li {
    float: left;
}

li a, .dropbtn {
    display: inline-block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    cursor: pointer;
}

li a:hover, .dropdown:hover .dropbtn {
    background-color: rgb(0, 0, 0);
}

li.dropdown {
    display: inline-block;
}

.dropdown-content {
    display: none;
    position: fixed;
    background-color: #383838;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 10;
}

.dropdown-content a {
    color: white;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
}

.dropdown-content a:hover {background-color: #1a1a1a}

.dropdown:hover .dropdown-content {
    display: block;
}
</style>
