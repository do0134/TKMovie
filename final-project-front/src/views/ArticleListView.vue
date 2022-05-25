<template>
  <div class="container">
    <h1 class="d-flex mt-5 mb-4">Community</h1>
    <div class="d-flex justify-content-between">
      <table class="table me-5">
        <thead>
          <tr>
            <th scope="col">번호</th>
            <th scope="col">제목</th>
            <th scope="col">작성자</th>
            <th scope="col">날짜</th>
            <th scope="col">좋아요 수</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="article in articles" :key="article.pk">
            <td>
              <span>{{ article.pk }}</span>
            </td>
            <td>
              <span>
                <router-link 
                  :to="{ name: 'article', params: {articlePk: article.pk} }">
                  {{ article.title }}
                </router-link>
              </span>
            </td>
            <td>
              <span>{{ article.user.username }}</span>
            </td>
            <td>
              <article-list-created :article="article"></article-list-created>
            </td>
            <td>
              <span>{{ article.like_count }}</span>
            </td>
          </tr>
        </tbody>
        <button v-if="isLoggedIn" @click="moveToNewArticle" class="my-3" id="new">New</button>
      </table>
      <div class="sub">
        <b-card border-variant="dark" header="인기 게시글" align="center" id="card">
          <ul class="ps-0">
            <li v-for="article in articles" :key="article.pk" class="mb-2 d-flex ms-5 ps-4">
              <router-link 
                :to="{ name: 'article', params: {articlePk: article.pk} }">
                {{ article.title }} 
              </router-link>
              <b-icon icon="suit-heart" aria-hidden="true" color="red" class="me-1 ms-3 mt-1"></b-icon>{{ article.like_count }}
            </li>
          </ul>
        </b-card>     
        <b-card border-variant="dark" header="댓글 많은 게시글" align="center" id="card">
          <ul class="ps-0">
            <li v-for="article in articles" :key="article.pk" class="mb-2 d-flex ms-5 ps-4">
              <router-link 
                :to="{ name: 'article', params: {articlePk: article.pk} }">
                {{ article.title }} 
              </router-link>
              <b-icon icon="suit-heart" aria-hidden="true" color="red" class="me-1 ms-3 mt-1"></b-icon>{{ article.like_count }}
            </li>
          </ul>
        </b-card>   
      </div>
    </div>
    
  </div>
  
  
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import ArticleListCreated from '@/components/ArticleListCreated.vue'

  export default {
    name: 'ArticleList',
    components : {
      ArticleListCreated
    },
    computed: {
      ...mapGetters(['articles', 'isLoggedIn'])
    },
    methods: {
      ...mapActions(['fetchArticles']),

      moveToNewArticle() {
        this.$router.push('/articles/new')
        
      },
      detailArticle() {
          console.log(this.articles)
        }

    },
    created() {
      this.fetchArticles(),
      this.detailArticle()
    },
  }
</script>

<style>
.sub {
  width: 30%;
}
.table {
  height: 80px;
}
#card {
  margin-top: 20px;
  margin-bottom: 20px;
}
#new {
  text-decoration: none;
  color: black;
  border: 0;
  box-shadow: none;
}
#card > div.card-header {
  background: rgb(253, 252, 226);
}
#card > div.card-body {
  height: 200px;
}
</style>
