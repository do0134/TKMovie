<template>
  <form @submit.prevent="onSubmit" class="comment-list-form d-flex justify-content-center">
    <div class="d-flex">
      <input type="text" id="review" v-model="content" required placeholder="리뷰를 남겨보세요!" onfocus="this.placeholder=''" onblur="this.placeholder='리뷰를 남겨보세요!'">
      <input class="mx-2" type="number" name="points" min="0" max="5" step="1" v-model="rating" required>
      <button class="btn btn-outline-warning btn-sm">Enter</button>
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