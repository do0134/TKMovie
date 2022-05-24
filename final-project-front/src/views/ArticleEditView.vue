<template>
  <div class="container">
    <h1 class="d-flex my-5">
      <b-button variant="link" :to="{ name: 'article', params: { params: { articlePk } } }" class="mx-3">
        <b-icon icon="arrow-left" aria-hidden="true" variant="dark" class="mt-1"></b-icon>
      </b-button>Edit Article</h1>
    <article-form v-if="isArticle" :article="article" action="update">

    </article-form>
  </div>

</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'AritcleEditView',
    components: { ArticleForm },
    computed: {
      ...mapGetters(['article', 'isArticle',])
    },
    methods: {
      ...mapActions(['fetchArticle'])
    },
    created() {
      this.fetchArticle(this.$route.params.articlePk)
    },
  }
</script>

<style></style>