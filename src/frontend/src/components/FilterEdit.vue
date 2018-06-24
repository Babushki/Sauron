<template>
    <div class="student-info" v-bind:class="{ opened: Object.values(this.$store.state.editWhitelist).length != 0 }">
        <h1>Edytuj:</h1>
        <h2>Nazwa:</h2>
        <input v-model="whitelistName"/>
        <h2>Procesy:</h2>
        <textarea v-model="whitelistAllowed"></textarea>
        <button v-on:click="saveWhitelist()">Zapisz</button>
        <h2>Grupa:</h2>
        <input v-model="whitelistGroup"/>
    </div>
</template>

<script>
export default {
  name: "FilterEdit",
  methods: {
    saveWhitelist: function() {
      this.$store.dispatch("saveWhitelist");
    }
  },
  computed:{
      whitelistName: {
          get() {
              return this.$store.state.editWhitelist.name
          },
          set(value) {
              this.$store.commit('updateEditWhitelistName', value)
          }
      },
        whitelistAllowed: {
          get() {
              return this.$store.state.editWhitelist.processes
          },
          set(value) {
              this.$store.commit('updateEditWhitelistAllowed', value)
          }
      },
        whitelistGroup: {
            get() {
              return this.$store.state.editWhitelist.group
          },
          set(value) {
              this.$store.commit('updateEditWhitelistGroup', value)
          }
        }
  }
};
</script>

<style scoped>
.student-info {
  text-align: center;
  width: 50%;
  background-color: lightgray;
  position: fixed;
  left: 100%;
  transition: 0.3s;
}
.opened {
  transform: translate(-100%, 0);
}
</style>
