<template>
  <div>
    
person-plus
    <h2>
      {{ profile.username }} 
      <b-button v-if="currentUser.username===profile.username" variant="light" :to="{ name: 'profileEdit', params: { username } }">
        <b-icon icon="gear-fill" aria-hidden="true"></b-icon> 프로필 편집
      </b-button>
      <b-button v-else variant="light" @click="following(followUsername)">
        <b-icon icon="person-plus" aria-hidden="true"></b-icon>
      </b-button></h2>
    <ul class="d-flex justify-content-center">
      <li class="my-list">게시글 {{ articleCount }}</li>
      <li class="my-list">팔로워 {{ followingCount }}</li>
      <li class="my-list">팔로우 {{ followersCount }}</li>
    </ul>
  </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: "MyProfile",
  data(){
    return{
      followUsername: this.$route.params.username,
    }
  },
  computed: {
    ...mapGetters(['profile', 'currentUser']),
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
    ...mapActions(['fetchProfile', 'following'])
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

