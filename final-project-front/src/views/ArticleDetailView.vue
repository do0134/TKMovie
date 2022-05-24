<template>
  <div class="container">
    <h1 class="d-flex mt-5 mb-4">Community</h1>
    <div class="d-flex justify-content-between">
      <b-button class="mt-2" variant="link" :to="{ name: 'articles' }" id="link">
        <b-icon icon="list" aria-hidden="true" variant="dark" class="me-1"></b-icon>목록으로
      </b-button>
      <p class="mt-3 me-3">
        <b-icon icon="suit-heart" aria-hidden="true" variant="dark" class="me-1"></b-icon>{{ likeCount }}
        <b-icon icon="chat-dots" aria-hidden="true" variant="dark" class="ms-2 me-1"></b-icon>{{ commentCount }}
      </p>
    </div>
    <hr class="mt-0" style="border: solid 2px;" id="hr">
    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <h2>{{ article.title }}</h2>
        <router-link :to="{ name: 'profile', params: { username: article.user.username } }" class="mt-2 ms-2">
          | {{ article.user.username }}</router-link>
      </div>
      <div class="d-flex">
        <b-button @click="[likeArticle(articlePk)]" variant="link" id="link" class="pe-0 pt-1">
          <b-icon v-if="changeLike===false" icon="heart" aria-hidden="true" variant="danger"></b-icon>
          <b-icon v-else icon="heart-fill" aria-hidden="true" variant="danger"></b-icon>
        </b-button>
        <p class="mt-2 ms-2">시간 넣기~</p>
      </div>
    </div>
    
    <hr>
    <p class="d-flex">
      {{ article.content }}
    </p>
    <!-- Article Edit/Delete UI -->
    <div class="d-flex justify-content-end">
      <!-- Article Like UI -->
      <div v-if="isAuthor && isLoggedIn">
        <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <b-button variant="link" id="link"><b-icon icon="pencil-square" aria-hidden="true" variant="dark"></b-icon> Edit</b-button>
        </router-link>
        |
        <b-button @click="deleteArticle(articlePk)" variant="link" id="link">
          <b-icon icon="trash" aria-hidden="true" variant="dark"></b-icon> Delete</b-button>
      </div>
      
    </div>
    
    <hr style="border: solid 2px;" id="hr">
    <!-- Comment UI -->
    <comment-list :comments="article.comments"></comment-list>

  </div>
</template>


<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article', 'isLoggedIn', 'currentUser']),
      likeCount() {
        return this.article.like_users?.length
      },
      commentCount() {
        return this.article.comments.length
      },
      
      changeLike(){
        return this.checkLike()
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
        'fetchCurrentUser'
      ]),
      checkLike(){
        for (let i of this.article.like_users){
          if (i.username === this.currentUser.username){
            return true
          } 
        } return false
      },
    },
    created() {
      this.fetchArticle(this.articlePk),
      this.checkLike()
    },
  }
</script>


<style>
#link { 
  text-decoration: none;
  color: black;
  border: 0;
  box-shadow: none;
}
#hr {
  color: rgb(255, 196, 0);
}
</style>