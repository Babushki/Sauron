<template>
    <div class="student-info" v-bind:class="{ opened: this.$store.state.student != null }">
        <h1>{{this.$store.state.student.name}}</h1>
        <span class="processess">
            <h2>Uruchomione procesy:</h2>
                <table class="table table-striped table-borderes">
                <thead>
                <tr>
                    <th>PID:</th>
                    <th>Nazwa:</th>
                    <th>Użytkownik:</th>
                </tr>
                </thead>
                <tbody>
                <tr v-bind:key="process.PID" v-for="process in this.$store.state.student.prosesses">
                    <td>{{process.PID}}</td>
                    <td>{{process.name}}</td>
                    <td>{{process.user}}</td>
                </tr>
                </tbody>
                <br/>
            </table>
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
