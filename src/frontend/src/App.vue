<template>
  <div id="app">
    <TopMenu/>
    <Body/>
  </div>
</template>

<script>
import Body from './components/Body'
import TopMenu from './components/TopMenu'

export default {
  name: 'App',
  components: {
    TopMenu,
    Body
  }
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Montserrat:400,700');
body {
  background-color: #EEEEEE;
  font-family: 'Montserrat', sans-serif;
  display: grid;
  grid-template-rows: auto;
  justify-items: center;
}
body, html {
  margin: 0;
  height: 100%;
}
#app {
    width: 100%;
    background-image: url('./assets/Sauron.svg');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: bottom right;
    background-size: 30%;
}

</style>
