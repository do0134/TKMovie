<template>
  <div class="container">
    <h1>여기는 프로필 편집</h1>
    <b-button variant="link" :to="{ name: 'profile', params: { username } }">
      <b-icon icon="backspace" aria-hidden="true" variant="dark"></b-icon>
    </b-button>
    
    <my-profile></my-profile>
  </div>
</template>


<script>
import MyProfile from '@/components/MyProfile.vue'
export default {
  components: { MyProfile },
}
</script>


<style>

</style>