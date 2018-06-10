<template>
  <div id="home">
    <TopMenu/>
    <Body v-if="this.$store.state.room !== 3333"/>
    <RoomSelect v-if="this.$store.state.room === 3333"/>
  </div>
</template>

<script>
import Body from "../components/Body";
import TopMenu from "../components/TopMenu";
import Footer from "../components/Footer";
import RoomSelect from "../components/RoomSelect";

export default {
  name: "Home",
  components: {
    TopMenu,
    Body,
    Footer,
    RoomSelect
  },
  mounted() {
    this.$store.dispatch('fetchRooms');
  }
};
</script>

<style>
</style>
