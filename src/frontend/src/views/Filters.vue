<template>
  <div id="filters">
    <TopMenu/>
    <FiltersManagement/>
  </div>
</template>

<script>
import FiltersManagement from "../components/FiltersManagement";
import TopMenu from "../components/TopMenu";
import Footer from "../components/Footer";

export default {
  name: "Filters",
  components: {
    TopMenu,
    FiltersManagement,
    Footer
  },
  mounted() {
    this.$store.dispatch('fetchWhitelists');
  }
};
</script>

<style>
</style>
