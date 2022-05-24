<template>
  <div class="container">
    <h1 class="d-flex my-5">
      <b-button variant="link" :to="{ name: 'profile', params: { username } }" class="mx-3">
        <b-icon icon="arrow-left" aria-hidden="true" variant="dark"></b-icon>
      </b-button>
      프로필 편집</h1>
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