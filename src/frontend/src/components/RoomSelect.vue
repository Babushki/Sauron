<template>
<div class="background">

    <header class="v-header container">
    <div class="fullscreen-video-wrap">
    </div>
    <div class="header-overlay"></div>
    <div class="header-content text-md-center">
        <center>
          <h1>Witaj w aplikacji Sauron!</h1>
          <h2> Wpisz grupę do monitorowania:</h2>
      
      <input  v-model="selected" >
      
      <a class="btn" type="submit" v-on:click="submit" > Wejdź do sali</a>
        </center>
    </div>
    </header>
</div>
</template>

<script>
import image from "../assets/background.jpg";
export default {
  name: "RoomSelect",
  data() {
    return {
      selected: ""
    };
  },
  mounted() {},
  methods: {
    submit: function() {
      this.$store.dispatch("chooseRoom", this.selected);
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
select {
  margin-top: 2em;
  margin-bottom: 2em;
}
.v-header {
  height: 100%;
  display: grid;
  color: #fff;
}

.header-overlay {
  height: 100%;
  position: absolute;
  left: 0;
  width: 100%;
  z-index: 1;
  background: #1d1918;
  opacity: 0.86;
}

.header-content {
  z-index: 2;
}

.header-content h1 {
  font-size: 50px;
  margin-bottom: 2em;
}

.btn {
  background: #8fd694;
  color: #fff;
  font-size: 1.2rem;
  padding: 1rem 2rem;
  cursor: pointer;
}
.btn:hover{
  opacity: .90;
}
select {
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
select option {
  padding: 0 4px;
}
select::-ms-expand {
  display: none;
}
select:focus {
  outline: none;
}
</style>
