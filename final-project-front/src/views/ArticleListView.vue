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
            <th scope="col"><b-icon icon="suit-heart" aria-hidden="true" class="me-1" style="color:hotpink"></b-icon></th>
            <th scope="col"><b-icon icon="chat-dots" aria-hidden="true" variant="success" class="me-1"></b-icon></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="article in articles" :key="article.pk">
            <td id="tableSub">
              <span>{{ article.pk }}</span>
            </td>
            <td>
              <span id="tableTitle">
                <p @click="goArticle(article)" id="a" class="mb-0" style="cursor:pointer">{{ article.title }}</p>
              </span>
            </td>
            <td id="tableUser">
              <p @click="goProfile(article)" id="a" class="mb-0" style="cursor:pointer">{{ article.user.username }}</p>
            </td>
            <td id="tableTime">
              {{ article.created_at.substr(0,10) }} <article-list-created :article="article"></article-list-created>
            </td>
            <td id="tableSub">
              <span>{{ article.like_count }}</span>
            </td>
            <td id="tableSub">
              <span>{{ article.comment_count }}</span>
            </td>
          </tr>
        </tbody>
        <b-button v-if="isLoggedIn" @click="moveToNewArticle" class="my-3" id="new" variant="link">
          <i class="fa-solid fa-star" style="color:gold"></i>New<i class="fa-solid fa-star" style="color:gold"></i></b-button>
      </table>
      <div class="sub">
        <popular-article></popular-article>     
        <many-comment></many-comment>   
      </div>
    </div>
    
  </div>
  
  
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import ArticleListCreated from '@/components/ArticleListCreated.vue'
  import PopularArticle from '@/components/PopularArticle.vue'
  import ManyComment from '@/components/ManyComment.vue'

  export default {
    name: 'ArticleList',
    components : {
      ArticleListCreated,
      PopularArticle,
      ManyComment
    },
    computed: {
      ...mapGetters(['article', 'articles', 'isLoggedIn'])
    },
    methods: {
      ...mapActions(['fetchArticles']),

      moveToNewArticle() {
        this.$router.push('/articles/new')
        
      },
      detailArticle() {
          console.log(this.articles)
        },
      goArticle(article) {
        this.$router.push({ name: 'article', params: {articlePk: article.pk} })
        console.log(this.article.pk)
      },
      goProfile(article) {
        this.$router.push({ name: 'profile', params: { username: article.user.username } })
      }

    },
    created() {
      this.fetchArticles(),
      this.detailArticle()
    },
  }
</script>

<style>
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
#tableTime {
  width: 200px;
}
#tableSub {
  width: 100px;
}
#tableTitle {
  width: 300px;
}
#tableUser {
  width: 150px;
}
</style>
