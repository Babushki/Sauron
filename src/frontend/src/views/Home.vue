<template>
  <div id="home">
    <TopMenu/>
    <Body/>
  </div>
</template>

<script>
import Body from '../components/Body'
import TopMenu from '../components/TopMenu'

export default {
  name: 'Home',
  components: {
    TopMenu,
    Body
  }
}
</script>

<style>

</style>
