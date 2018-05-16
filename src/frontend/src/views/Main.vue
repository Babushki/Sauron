<template>
  <div id="home">
    <TopMenu/>
    <MainBody/>
  </div>
</template>

<script>
import MainBody from '../components/MainBody'
import TopMenu from '../components/TopMenu'
import Footer from '../components/Footer'

export default {
  name: 'Main',
  components: {
    TopMenu,
    MainBody,
    Footer
  }
}
</script>

<style>

</style>
