<template>
<div>
  <ul>
  <li class="dropdown">
    <a class="dropbtn">Whitelist</a>
    <div class="dropdown-content">
      <a v-for="(data,index) in whitelists" :key='index'>
          <a>{{data.Whitelist}}</a>
      </a>
    </div>
  </li>
  <li class="dropdown">
    <a class="dropbtn">Sala</a>
    <div class="dropdown-content">
      <a v-for="(data,index) in rooms" :key='index'>
          <a>{{data.Room}}</a>
      </a>
    </div>
  </li>
  <li style="float:right">
    <a>
        Ustawienia
    </a>
  </li>
  
</ul>
</div>
</template>

<script>

export default {
        name: 'TopMenu',
        data () {
            return {
                whitelists:[
                    {"Whitelist": "C++ Klokwium"},
                    {"Whitelist": "Java Kolokwium"},
                    {"Whitelist": "Zaliczenie"},
                    {"Whitelist": "Coś innego"}
                ],
                rooms:[
                    {"Room": "216"},
                    {"Room": "217"},
                    {"Room": "218"}
                ]
            }
        },
        mounted() {
            this.$http.get("https://httpbin.org/bytes/1").then(result => {
                this.res = result.body.uuid;
            }, error => {
                console.error(error);
            });
        },
        methods: {
            sendData() {
                this.$http.post("https://httpbin.org/post", this.input, { headers: { "content-type": "application/json" } }).then(result => {
                    this.response = result.body.data;
                }, error => {
                    console.error(error);
                });
            },
            getData(){
                this.$http.get("https://httpbin.org/bytes/3").then(result => {
                this.res = result.body.uuid;
            }, error => {
                console.error(error);
            });
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
