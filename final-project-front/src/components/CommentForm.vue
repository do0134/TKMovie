<template>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <label for="comment" class="d-flex">
      {{ currentUser.username }} 님의 댓글 <b-icon icon="chat-text" variant="dark" class="ms-2"></b-icon></label>
    <div class="d-flex">
      <input type="text" id="comment" v-model="content" required class="me-1 my-3">
      <button class="btn btn-outline-warning btn-sm my-3 enter">Enter</button>
    </div>
    
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article', 'currentUser']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>
#comment{
  width:100%;
  border: 1px solid #2e4a67;
  padding: 16px;
  background: #fff;
}
.enter {
  height: 60px;
}
</style>