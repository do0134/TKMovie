<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="secondary">
      <b-navbar-brand to="/">Home</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav class="justify-content-between">
        <b-navbar-nav>
          <b-nav-item to="/articles">Community</b-nav-item>
          <b-nav-item to="#">Recommendation</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="isLoggedIn" class="ml-auto">
          <!-- 검색 버튼 추가하기 -->
          <!-- <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form> -->
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
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
          <!-- 검색 버튼 추가하기 -->
          <!-- <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form> -->

          <b-nav-item to="/login">Login</b-nav-item>
          <b-nav-item to="/signup">SignUp</b-nav-item>

          <!-- 회원가입 부분을 모달창으로 띄워볼까? -->
          <!-- <b-modal id="sing-up" hide-footer>
            <template #modal-title>
              SignUp
            </template>
            <form @submit.prevent="signup(credentials)">
              <div>
                <label for="username">Username: </label>
                <input  v-model="credentials.username" type="text" id="username" required/>
              </div>
              <div>
                <label for="password1">Password: </label>
                <input v-model="credentials.password1" type="password" id="password1" required />
              </div>
              <div>
                <label for="password2">Password Confirmation:</label>
                <input v-model="credentials.password2" type="password" id="password2" required />
              </div>
              <div>
                <button>Signup</button>
              </div>
            </form>
            <b-button class="mt-3" block @click="$bvModal.hide('sing-up')">Close Me</b-button>
          </b-modal> -->
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>

</template>


<script>
import { mapGetters } from 'vuex'
  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    }
  }
</script>


<style>

</style>