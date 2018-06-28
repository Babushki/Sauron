<template>
  <div id="login">
    <h1>Login</h1>
    <form>
        <input type="text" v-model="login" placeholder="Login"/>
        <input type="password" v-model="password" placeholder="Hasło"/>
        <button type="submit" v-on:click="submitLogin" >Zaloguj</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      login: "",
      password: ""
    };
  },
  methods: {
    submitLogin: function(event) {
      event.preventDefault();
      this.$store
        .dispatch("login", { login: this.login, password: this.password })
        .then(() => {
          if (this.$store.state.logged) {
            this.$router.push("/home");
          }
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#login {
  text-align: center;
}

h1 {
  font-size: 4em;
}

form {
  display: flex;
  flex-direction: column;
  margin: auto;
  width: 400px;
}

form input {
  font-size: 2em;
  margin: 5px 0;
}

form button {
  font-size: 2em;
  margin: 15px 0;
}
</style>