<template>
  <div>
    
person-plus
    <h2>
      {{ profile.username }} 
      <b-button variant="light" :to="{ name: 'profileEdit', params: { username } }">
        <b-icon icon="gear-fill" aria-hidden="true"></b-icon> 프로필 편집
      </b-button></h2>
    <ul class="d-flex justify-content-center">
      <li class="my-list">게시글 {{ articleCount }}</li>
      <li class="my-list">팔로워 {{ followersCount }}</li>
      <li class="my-list">팔로우 {{ followingCount }}</li>
    </ul>
  </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: "MyProfile",
  computed: {
    ...mapGetters(['profile']),
    articleCount() {
        return this.profile.articles.length
      },
    followersCount() {
        return this.profile.followers.length
      },
    followingCount() {
        return this.profile.following.length
      },
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
.my-list{
  list-style-type: none;
  margin : 20px;
}
</style>

