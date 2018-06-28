<template>
    <div class="error">
        <label>Wystąpił błąd</label>
        <p>{{this.$store.state.errorMessage}}</p>
    </div>
</template>

<script>
export default {
  name: "Error"
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.error {
  position: absolute;
  top: 15px;
  right: 15px;
  width: 250px;
  text-align: left;
  border: 3px solid #cc0000;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  padding: 5px;
}

.error label {
    text-align: left;
}

.error p {
    text-align: left;
}
</style>