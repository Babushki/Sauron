<template>
    <div class="student-info" v-bind:class="{ opened: this.$store.state.student != null }">
        <h1>Marek Hucz</h1>
        <span class="processess">
            <h2>Uruchomione procesy:</h2>
            <ul>
                <li>systemd</li>
                <li>kthread</li>
                <li>python3</li>
            </ul>
        </span>
    </div>
</template>

<script>
export default {
  name: "StudentInfo"
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
