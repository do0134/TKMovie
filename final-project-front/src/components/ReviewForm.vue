<template>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <label for="review" class="d-flex">
      {{ currentUser.username }}</label>
    <div class="d-flex">
      <input type="text" id="review" v-model="content" required>
      <input type="number" name="points" min="0" max="5" step="1" v-model="rating" required>
      <button>Enter</button>
    </div>
    
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewForm',
  components: {

  },
  props:{
    movie:Object
  },
  data() {
    return {
      content: '',
      rating : 0,
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ moviePk: this.movie.id, content: this.content, rating: this.rating, })
      this.content = ''
      this.rating = 0
    },
  },

}
</script>

<style >
 
</style>