<template>
  <div id="main-container">
    <Loader v-if="this.$store.state.loading"/>
    <Error v-if="this.$store.state.error" />
    <div id="app" v-bind:class="{ disabled: this.$store.state.loading }">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Loader from './components/Loader'
import Error from './components/Error'

export default {
  name: 'App',
  components: {
    Loader,
    Error
  }
}
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Montserrat:400,700");
body {
  background-color: #eeeeee;
  font-family: "Montserrat", sans-serif;
  display: grid;
  grid-template-rows: auto;
  justify-items: center;
}
body,
html {
  margin: 0;
  height: 100%;
}
.disabled {
  opacity: 0.3;
}
#app {
  width: 100%;
  height: 100%;
  background-image: url("./assets/Sauron.svg");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: bottom left;
  background-size: 30%;
}
#main-container {
  width: 100%;
}
</style>
