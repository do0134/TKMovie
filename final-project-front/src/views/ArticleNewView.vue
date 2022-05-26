<template>
  <div class="container">
    <h1 class="d-flex my-5">
      <b-button variant="link" :to="{ name: 'articles' }" class="mx-3 mt-0.5">
        <b-icon icon="arrow-left" aria-hidden="true" variant="dark" class="mt-1"></b-icon>
      </b-button><h1 class="communitytitle">New Article</h1></h1>
    <article-form :article="article" action="create"></article-form>
  </div>
</template>

<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'AritcleNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style></style>
