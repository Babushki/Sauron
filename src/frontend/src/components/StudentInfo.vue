<template>
    <div class="student-info" v-bind:class="{ opened: Object.values(this.$store.state.student).length != 0 }">
        <h1>{{this.$store.state.student.nazgul}}</h1>
        <span class="processess">
            <img class="screenshot" :src="'data:image/png;base64, ' + this.$store.state.studentsScreenshots[this.$store.state.student.nazgul]" alt="Screenshot" />
            
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
                <tr v-bind:key="process.pid" v-for="process in this.$store.state.student.processes">
                    <td>{{process.pid}}</td>
                    <td>{{process.name}}</td>
                    <td>{{process.username}}</td>
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
    position: relative;
    left: 100%;
    transition: 0.3s;
}
.opened {
    transform: translate(-200%, 0);
}

.screenshot {
    width: 100%;
}
</style>
