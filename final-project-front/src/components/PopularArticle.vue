<template>
  <div>
    <b-card border-variant="dark" header="인기 게시글(TOP 5)" align="center" id="card">
      <ul class="ps-0">
        <li v-for="article in pArticles" :key="article.pk" class="mb-2 d-flex ms-3">
          <p @click="goArticle" style="cursor:pointer" id="a">{{ article.title }} </p>
          <b-icon icon="suit-heart" aria-hidden="true" class="me-1 ms-3 mt-1" style="color:hotpink"></b-icon>{{ article.like_count }}
        </li>
      </ul>
    </b-card>
  </div>
</template>
<script>
  import { mapGetters } from 'vuex'
  import _ from 'lodash'

  export default {
    name: "PopularArticle",
    data() {
      return {
        pArticles: []
      }
    },
    computed: {
      ...mapGetters(['articles', 'article'])
      
    },
    methods: {
      getPArticles() {
        this.pArticles = _.sortBy(this.articles, 'like_count').reverse().slice(0,5)
      },
      goArticle() {
        this.$router.push({ name: 'article', params: {articlePk: this.article.pk} })
      }
    },
    created(){
      this.getPArticles()
    },
  }
</script>

<style>
#card {
  width: 300px;
}
</style>