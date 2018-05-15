<template>
      <div class="container">
          <br/>
            <h1> Aktualnie podłączeni użytkownicy do sali {{ip}}</h1>
       <a>
        <a>{{ res }}</a>
        <br/>
        <button v-on:click="sendData()">Podgląd</button>
        <button v-on:click="getData()">Zbanuj</button>
        <br/>
      </a>
    </div>
</template>

<script>
export default {
  name: "Body",
  data() {
    return {
      ip: "",
      res: "",
      input: {
        firstname: "",
        lastname: ""
      },
      response: {
        firstname: "",
        lastname: ""
      }
    };
  },
  mounted() {
    this.$http.get("https://httpbin.org/ip").then(
      result => {
        this.ip = result.body.origin;
      },
      error => {
        console.error(error);
      }
    );
    this.$http.get("https://httpbin.org/uuid").then(
      result => {
        this.res = result;
      },
      error => {
        console.error(error);
      }
    );
  },
  methods: {
    sendData() {
      this.$http
        .post("https://httpbin.org/post", this.input, {
          headers: { "content-type": "application/json" }
        })
        .then(
          result => {
            this.response = result.body.data;
          },
          error => {
            console.error(error);
          }
        );
    },
    getData() {
      this.$http.get("https://httpbin.org/uuid").then(
        result => {
          this.res = result.body.uuid;
        },
        error => {
          console.error(error);
        }
      );
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  text-align: center;
  margin-left: 10%;
  height: 100%;
  background-color: lightgray;
  width: 400px;
}
textarea {
  height: 100px;
  width: 200px;
}
</style>
