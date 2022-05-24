<template>
  <div class="container">
    <h1 class="d-flex my-5">My Page</h1>
    <my-profile/>
      <div class="d-flex justify-content-center">
        <b-card border-variant="dark" header="작성한 글" align="center" id="card">
          <ul class="ps-0">
            <li v-for="article in profile.articles" :key="article.pk">
              <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
                {{ article.title }}
              </router-link>
            </li>
          </ul>
        </b-card>     
        <b-card border-variant="dark" header="좋아요 한 글" align="center" id="card">
          <ul class="ps-0">
            <li v-for="article in profile.like_articles" :key="article.pk">
              <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
                {{ article.title }}
              </router-link>
            </li>
          </ul>
        </b-card>          
      </div>
    <!-- <div class="d-flex justify-content-between">
      <div>
        <h2>작성한 글</h2>
        <ul>
          <li v-for="article in profile.articles" :key="article.pk">
            <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.title }}
            </router-link>
          </li>
        </ul>
      </div>
      <div>
        <h2>좋아요 한 글</h2>
        <ul>
          <li v-for="article in profile.like_articles" :key="article.pk">
            <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.title }}
            </router-link>
          </li>
        </ul>
      </div>
    </div> -->
    
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MyProfile from '@/components/MyProfile.vue'


export default {
  name: 'ProfileView',
  components : {
    MyProfile
  },
  computed: {
    ...mapGetters(['profile']),
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
#card {
  height: 400px; width: 295px;
}
</style>