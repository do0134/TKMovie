<template>
  <div>
    <b-card border-variant="dark" header="댓글 많은 게시글" align="center" id="card">
      <ul class="ps-0">
        <li v-for="article in cArticles" :key="article.pk" class="mb-2 d-flex ms-3">
          <router-link 
            :to="{ name: 'article', params: {articlePk: article.pk} }">
            {{ article.title }} 
          </router-link>
          <b-icon icon="chat-dots" aria-hidden="true" variant="success" class="me-1 ms-3 mt-1"></b-icon>{{ article.like_count }}
        </li>
      </ul>
    </b-card>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  import _ from 'lodash'

  export default {
    name: 'ManyComment',
    data() {
      return {
        cArticles: []
      }
    },
    computed: {
      ...mapGetters(['articles'])
    },
    methods: {
      getCArticles() {
        this.cArticles = _.sortBy(this.articles, 'comment_count').reverse().slice(0,5)
      },
      
    },
    created() {
      this.getCArticles()
    }
  }
</script>

<style>
#card {
  width: 300px;
}
</style>