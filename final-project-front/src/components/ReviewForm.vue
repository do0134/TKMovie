<template>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <label for="review" class="d-flex">
      {{ currentUser.username }}</label>
    <div class="d-flex">
      <input type="text" id="review" v-model="content" required>
      <button>Enter</button>
    </div>
    
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['movie', 'currentUser']),
  },
  methods: {
    ...mapActions(['createreview']),
    onSubmit() {
      this.createreview({ moviePk: this.movie.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>

</style>