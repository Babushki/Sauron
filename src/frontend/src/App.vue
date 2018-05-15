<template>
  <div id="app">
    <router-view/>
  </div>
</template>

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
#app {
  width: 100%;
  background-image: url("./assets/Sauron.svg");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: bottom right;
  background-size: 30%;
}
</style>
