<template>
<div>
  <ul>
      <li>
          <router-link to="/home"><button>Podlgąd sali</button></router-link>
      </li>
  <li class="dropdown">
    <a class="dropbtn" v-if="this.$store.state.whitelist !== ''">Wybrany filtr: {{this.$store.state.whitelist.name}}</a>
    <a v-else> Brak wybranego filtru</a>
    <div class="dropdown-content">
      <a v-for="(data,index) in this.$store.state.whitelists" :key='index'>
          <a v-on:click="submitWhitelist(data)">{{data.name}}</a>
      </a>
      <router-link to="/filters">Zarządzaj filtrami</router-link>
    </div>
  </li>
  <li class="dropdown">
   <a  v-if="this.$store.state.room !== 3333" class="dropbtn">Wybrana sala: {{this.$store.state.rooms[this.$store.state.room].name}}</a>
    <a v-else>Brak wybranej sali</a>
    <div class="dropdown-content">
      <a  v-for="(data,index) in this.$store.state.rooms" :key='index' >
          <a v-on:click="submitRoom(data.id)">{{data.name}}</a>
      </a>
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
                
            }
        },
        mounted() {
             this.$store.dispatch('fetchWhitelists');
             this.$store.dispatch('fetchRooms');
        },
        methods: {
            logout() {
                this.$store.dispatch('logout').then(() => {
                    this.$router.push('/')
                })
            },
            submitRoom: function(room){
            this.$store.dispatch("chooseRoom", room).then(()=>
            {
                console.log(this.$store.state.room);
            })
            },
            submitWhitelist: function(whitelist){
            this.$store.dispatch("chooseWhitelist", whitelist).then(()=>
            {
                console.log(this.$store.state.whitelist);
            })
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
