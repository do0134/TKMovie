<template>
  <div class="container">
    <h1 class="d-flex my-5 communitytitle">Profile</h1>
    <my-profile/>
      <div class="d-flex justify-content-center">
        <b-card border-variant="dark" header="작성한 글" align="center" id="mycard">
          <ul class="ps-0">
            <li v-for="article in profile.articles" :key="article.pk" class="my-list">
              <p @click="goArticle" style="cursor:pointer" id="a">{{ article.title }}</p>
            </li>
          </ul>
        </b-card>     
        <b-card border-variant="dark" header="좋아요 한 글" align="center" id="mycard">
          <ul class="ps-0">
            <li v-for="article in profile.like_articles" :key="article.pk" class="my-list">
              <p @click="goArticle" style="cursor:pointer" id="a">{{ article.title }}</p>
            </li>
          </ul>
        </b-card>          
      </div>
    
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
    ...mapGetters(['profile', 'article']),
  },
  methods: {
    ...mapActions(['fetchProfile']),
    goArticle() {
      this.$router.push({ name: 'article', params: {articlePk: this.article.pk} })
    }
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  }
}
</script>
<style>
.my-list{
  list-style-type: none;
}
#mycard > div.card-header {
  background: rgb(253, 252, 226);
}
#mycard {
  margin: 0px 20px;
  width: 400px;
}
</style>