<template>
    <div class="loader">
      <div>
      </div>
    </div>
</template>

<script>
export default {
  name: "Loader"
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.loader {
  position: absolute;
  top: 25%;
  left: 50%;
  z-index: 100;
}

.loader > div {
  position: relative;
  top: -50%;
  left: -50%;
  border: 16px solid #444;
  border-top: 16px solid rgba(0, 0, 0, 0);
  border-radius: 50%;
  width: 120px;
  height: 120px;
  animation: spin 1.5s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>