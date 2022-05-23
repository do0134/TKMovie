<template>
  <div class="container">
    <h1>Community</h1>
    <b-button variant="link" :to="{ name: 'article', params: {articlePk: article.pk -1} }" id="link">
      <b-icon icon="chevron-up" aria-hidden="true" variant="dark"></b-icon>((((얘는 넣을까 말까..))))
    </b-button>
    <b-button variant="link" :to="{ name: 'article', params: {articlePk: article.pk +1} }" id="link">
      <b-icon icon="chevron-down" aria-hidden="true" variant="dark"></b-icon>((((얘는 넣을까 말까..))))
    </b-button>
    <b-button variant="link" :to="{ name: 'articles' }" id="link">
      <b-icon icon="list" aria-hidden="true" variant="dark"></b-icon> 목록으로
    </b-button>
    <hr style="border: solid 2px red;">
    <h2 class="d-flex">{{ article.title }}</h2>
    <div class="d-flex">
      <div>
        {{ article.user.username }}
      </div>
      <div>

      </div>
    </div>
    <hr>
    <p>
      {{ article.content }}
    </p>
    <hr>
    <!-- Article Edit/Delete UI -->
    <div v-if="isAuthor && isLoggedIn">
      <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteArticle(articlePk)">Delete</button>
    </div>
    

    <!-- Article Like UI -->
    <div>
      Likeit:
      <button
        @click="likeArticle(articlePk)"
      >{{ likeCount }}</button>
    </div>

    <hr />
    <!-- Comment UI -->
    <comment-list :comments="article.comments"></comment-list>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  // import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article', 'isLoggedIn']),
      likeCount() {
        return this.article.like_users?.length
      }
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
