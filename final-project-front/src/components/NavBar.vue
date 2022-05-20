<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
      <div class="container-fluid d-flex justify-content-between my-2">
        <div>
          <ul class="navbar-nav">
            <li class="nav-item mx-3">
              <router-link to="/" class="text-white">Home</router-link>
            </li>
            <li class="nav-item mx-3">
              <router-link to="/articles" class="text-white">Community</router-link>
            </li>
            <li class="nav-item mx-3">
              <router-link to="#" class="text-white">Recommendation</router-link>
            </li>
          </ul>
        </div>
        <div>
          <ul class="navbar-nav">
            <li class="nav-item mx-3">
              <router-link to="#" class="text-white">Search</router-link>
            </li>
            <li class="nav-item mx-3">
              <router-link to="/login" class="text-white">Login</router-link>
            </li>
            <li class="nav-item mx-3">
              <router-link to="/signup" class="text-white">SignUp</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- <nav class="d-flex justify-content-center align-content-end">
      <p>바닥</p>
    </nav> -->
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>