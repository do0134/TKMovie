<template>
  <div>
    <li class="comment-list-item d-flex justify-content-around">
      <div></div>
      <div>
        <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
          {{ comment.user.username }}
        </router-link>님의 댓글 
        <span v-if="!isEditing" class="ms-3">
          <b-icon icon="chat-square-quote-fill" variant="warning" class="me-1"></b-icon>{{ payload.content }}</span>
      </div>
      

      <div class="d-flex justify-content-end">
        <span v-if="isEditing">
          <input type="text" v-model="payload.content">
          <button @click="onUpdate" class="btn-sm btn btn-light">
            <b-icon icon="check-lg" variant="dark" class="me-1"></b-icon></button> |
          <b-button @click="switchIsEditing" class="btn-sm btn btn-light">
            <b-icon icon="x-lg" variant="dark" class="me-1"></b-icon></b-button>
        </span>

        <span v-if="currentUser.username === comment.user.username && !isEditing">
          <button @click="switchIsEditing" variant="link" class="btn-sm btn btn-light">
            <b-icon icon="pencil-square" aria-hidden="true" variant="dark"></b-icon></button> |
          <button @click="deleteComment(payload)" variant="link" class="btn-sm btn btn-light">
            <b-icon icon="trash" aria-hidden="true" variant="dark"></b-icon></button>
        </span>
      </div>
    </li>
    <hr>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
</style>