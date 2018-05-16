<template>
<div class="background">

    <header class="v-header container">
    <div class="fullscreen-video-wrap">
    </div>
    <div class="header-overlay"></div>
    <div class="header-content text-md-center">
        <center>
      <h1> Wybierz pokój:</h1>
      
      <select  v-model="selected" >
          <option value="" disabled selected>...</option>
        <option  v-for="(data,index) in rooms" :key='index' > {{data.Room}}</option>
      </select>
      
      <a class="btn" type="submit" v-on:click="submit" > Wejdź do pokoju</a>
        </center>
    </div>
    </header>
</div>
</template>

<script>
import image from "../assets/background.jpg";
export default {
  name: "MainBody",
  data() {
    return {
      selected: '',
      rooms: [{ Room: "216" }, { Room: "217" }, { Room: "218" }]
    };
  },
  mounted() {},
  methods: {
      submit: function(){
         this.$router.push('/home')
      }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.background {
    background-size: cover !important;
  background-repeat: no-repeat !important;
  background-image: url("../assets/background.jpg") !important;
  width: 100%;
  height: 100vh;
  background-repeat: no-repeat;
  background-attachment: fixed;
}
select{
    margin-top: 2em;
    margin-bottom: 2em;
}
.v-header{
  height:100%;
  display:grid;
  color:#fff;
}



.header-overlay{
  height:100%;
  position: absolute;
  top:3em;
  left:0;
  width:100%;
  z-index:1;
  background:#1d1918;
  opacity:0.86;
}

.header-content{
  z-index:2;
}

.header-content h1{
  font-size:50px;
  margin-bottom:3em;
}

.btn{
  background: #8fd694;
  color:#fff;
  font-size:1.2rem;
  padding: 1rem 2rem;
}
select{
    display: block;
    padding: 10px 70px 10px 13px !important;
    max-width: 100%;
    height: auto !important;
    border: 1px solid #383838;
    border-radius: 3px;
    background-color: #383838;
    color: white;
    font-size: 22px;
    line-height: 16px !important;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
}
select option{
    padding: 0 4px;
}
select::-ms-expand{
    display: none;
}
select:focus{
    outline: none;
}
</style>
