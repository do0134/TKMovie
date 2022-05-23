<template>
  <div>
    <h1>Community</h1>
    <p>번호랑 시간 왜 안 나오죠?</p>
    <div class="d-flex justify-content-between">
      <table class="table">
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
              <span>{{ article.created_at }}</span>
            </td>
            <td>
              <span>{{ article.like_count }}</span>
            </td>
          </tr>
        </tbody>
      </table>
      <div>
        <div>
          <h4>인기 게시글(현재는 기본 게시글)</h4>
          <ul>
            <li v-for="article in articles" :key="article.pk">
              <router-link 
                :to="{ name: 'article', params: {articlePk: article.pk} }">
                {{ article.title }}
              </router-link>
            </li>
          </ul>
        </div>
        <div>
          <h4>댓글 많은 게시글(현재는 기본 게시글)</h4>
          <ul>
            <li v-for="article in articles" :key="article.pk">
              <router-link 
                :to="{ name: 'article', params: {articlePk: article.pk} }">
                {{ article.title }}
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
    
    <button v-if="isLoggedIn" @click="moveToNewArticle">New</button>
  </div>
  
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
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

<style></style>
