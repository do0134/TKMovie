<template>
  <div>
    <h1>
      {{ profile.username }} 
      <b-button variant="light" :to="{ name: 'profileEdit', params: { username } }">
        <b-icon icon="gear-fill" aria-hidden="true"></b-icon> 프로필 편집
      </b-button></h1>
    <ul class="d-flex justify-content-center">
      <p>((((((((((장고 완성하면 게시글 수, 팔로워 팔로우 수 넣기))))))))))</p>
      <li class="my-list">게시글</li>
      <li class="my-list">팔로워</li>
      <li class="my-list">팔로우</li>
    </ul>
  </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: "MyProfile",
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>


<style>

</style>

