<template>
  <div>
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
      <div>
        <!-- <div>
          <b-button v-b-modal.modal-scrollable>Show Modal</b-button>
          <b-modal id="modal-scrollable" scrollable title="Scrollable Content" ok-only>
            <p v-for="article in articles" :key="article.pk">{{  }}</p>
            <p @click="goProfile" id="a" class="ms-3 mt-2" style="cursor:pointer">{{  }}</p>
          </b-modal>
        </div> -->
      </div>
      <li class="my-list">팔로워 {{ followersCount }}</li>
      <li class="my-list">팔로우 {{ followingCount }}</li>
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

        return this.profile.follower_count
      },
    followingCount() {

        return this.profile.following_count
      },
  },
  methods: {
    ...mapActions(['fetchProfile', 'following'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
    console.log(this.profile)
  },
  // goProfile() {
  //   this.$router.push({ name: 'profile', params: { username: this.article.user.username } })
  // }
}
</script>


<style>
.my-list{
  list-style-type: none;
  margin : 20px;
}
</style>

