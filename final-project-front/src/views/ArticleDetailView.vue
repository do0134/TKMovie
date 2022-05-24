<template>
  <div class="container">
    <h1 class="d-flex mt-5 mb-4">Community</h1>
    <b-button class="d-flex" variant="link" :to="{ name: 'articles' }" id="link">
      <b-icon icon="list" aria-hidden="true" variant="dark" class="me-1"></b-icon>목록으로
    </b-button>
    <hr style="border: solid 2px black;">
    <div class="d-flex justify-content-between">
      <h2>{{ article.title }}</h2>
      <p class="mt-2">
        <b-icon icon="suit-heart" aria-hidden="true" variant="dark" class="me-1"></b-icon>{{ likeCount }}
        <b-icon icon="chat-dots" aria-hidden="true" variant="dark" class="ms-2 me-1"></b-icon>{{ commentCount }}
      </p>
    </div>
    
    <div class="d-flex justify-content-between">
      <div>
        <router-link :to="{ name: 'profile', params: { username: article.user.username } }">{{ article.user.username }}</router-link>
      </div>
      <div>
        <p>시간 넣기~</p>
      </div>
    </div>
    <hr>
    <p class="d-flex">
      {{ article.content }}
    </p>
    <hr>
    <!-- Article Edit/Delete UI -->
    <div class="d-flex justify-content-between">
      <!-- Article Like UI -->
        <div>
          Likeit:
          <button
            @click="likeArticle(articlePk)"
          >{{ likeCount }}</button>
        </div>
      <div v-if="isAuthor && isLoggedIn">
        <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <b-button variant="light"><b-icon icon="pencil-square" aria-hidden="true" variant="dark"></b-icon> Edit</b-button>
        </router-link>
        |
        <b-button @click="deleteArticle(articlePk)" variant="light">
          <b-icon icon="trash" aria-hidden="true" variant="dark"></b-icon> Delete</b-button>
      </div>
      
    </div>
    
    <hr style="border: solid 2px black;">
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
      ...mapGetters(['isAuthor', 'article', 'isLoggedIn']),
      likeCount() {
        return this.article.like_users?.length
      },
      commentCount() {
        return this.article.comments.length
      },
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style>
#link { 
  text-decoration: none;
  color: black;
}
</style>
