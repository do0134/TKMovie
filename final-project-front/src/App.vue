<template>
  <div id="app">
    <nav-bar/>
    <router-view/>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'

  export default {
    name: 'App',
    components: { NavBar },
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
#app > div.bg-dack {
  background-color: rgb(0, 0, 0);
}
nav {
  padding: 50px;
  height: 150px;;
}

nav a {
  font-weight: bold;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
