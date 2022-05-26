<template>
  <div class="bg-dack">
    <b-navbar toggleable="lg" type="dark">
      <b-icon @click="goHome()" style="cursor:pointer" icon="camera-reels" variant="danger" font-scale="4" class="ms-2 animate__animated animate__jackInTheBox animate__infinite"></b-icon>
      <b-navbar-brand to="/" class="text-danger ms-4 mt-4" style="font-size: 30px;">TKmovie</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav class="justify-content-between mt-4 pt-2" style="font-size: 20px;">
        <b-navbar-nav>
          <b-nav-item to="/articles">Community</b-nav-item>
          <b-nav-item to="/movie/movie_worldcup">Movie World Cup<b-icon class="ms-1" icon="star-fill" animation="fade" style="color:gold"></b-icon></b-nav-item>
        </b-navbar-nav>
        
        <b-navbar-nav v-if="isLoggedIn" class="ml-auto">
          <b-nav-item-dropdown right>
            <template #button-content>
              <b-avatar variant="dark"></b-avatar>
              <em>{{ currentUser.username }}</em>
            </template>
            <b-dropdown-item :to="{ name: 'profile', params: { username } }" variant="outline-warning " class="mb-2">
              <b-icon icon="person-circle" aria-hidden="true"></b-icon> My Page
            </b-dropdown-item>
            <b-dropdown-item :to="{ name: 'logout' }" variant="outline-warning " class="mb-2">
              <b-icon icon="power" aria-hidden="true"></b-icon> Logout
            </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>

        <b-navbar-nav v-else class="ml-auto">
          <b-nav-item to="/login">Login</b-nav-item>
          <b-nav-item to="/signup">SignUp</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    
  </div>

</template>


<script>
import { mapGetters } from 'vuex'
import 'animate.css'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods: {
      goHome() {
        this.$router.push({ name: 'main' })
      }
    }
  }
</script>


<style>

</style>