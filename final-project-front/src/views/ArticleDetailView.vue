<template>
  <div class="container">
    <h1>Community</h1>
    <b-button class="d-flex" variant="link" :to="{ name: 'articles' }" id="link">
      <b-icon icon="list" aria-hidden="true" variant="dark" class="me-1"></b-icon>목록으로
    </b-button>
    <hr style="border: solid 2px black;">
    <div class="d-flex justify-content-between">
      <h2>{{ article.title }}</h2>
      <p class="mt-2">
        <b-icon icon="suit-heart" aria-hidden="true" variant="dark" class="me-1"></b-icon>{{ likeCount }}
        <b-icon icon="chat-dots" aria-hidden="true" variant="dark" class="ms-2 me-1"></b-icon> 댓글 개수 넣기~
      </p>
    </div>
    
    <div class="d-flex justify-content-between">
      <div>
        {{ article.user.username }}
      </div>
      <div>
        <p>시간 넣기~</p>
      </div>
    </div>
    <hr>
    <p>
      {{ article.content }}
    </p>
    <hr>
    <!-- Article Edit/Delete UI -->
    <div class="d-flex justify-content-between">
      <div v-if="isAuthor && isLoggedIn">
        <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <button><b-icon icon="pencil-square" aria-hidden="true" variant="dark"></b-icon> Edit</button>
        </router-link>
        |
        <button @click="deleteArticle(articlePk)">
          <b-icon icon="trash" aria-hidden="true" variant="dark"></b-icon> Delete</button>
      </div>
      

      <!-- Article Like UI -->
      <div>
        Likeit:
        <button 
          @click="[likeArticle(articlePk), checkLike()]"
        >{{ likeCheck }}</button>

        <!-- <b-button variant="link" @click="[likeArticle(articlePk), liking()]">
          <b-icon  v-if="isLiking" icon="suit-heart-fill" aria-hidden="true" variant="dark"></b-icon>
          <b-icon v-else icon="suit-heart" aria-hidden="true" variant="dark"></b-icon>
        </b-button> -->
      </div>
    </div>
    

    <hr />
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
        articlePk: this.$route.params.articlePk,
        isLike : false
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article', 'isLoggedIn','currentUser']),
      likeCount() {
        return this.article.like_users?.length
      },
      likeCheck(){
        if(this.isLike===true){
          return true
        } else{
          return false
        }
      }
      // commentCount() {
      //   return this.comment.length
      // },
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
        'fetchCurrentUser',
      ]),
      checkLike(){
        for(let i of this.article.like_users){
          if(i.username==this.currentUser.username){
            this.isLike = true
            console.log(this.isLike)
          }
        }
      }
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
}
</style>
