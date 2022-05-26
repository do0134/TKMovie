<template>
  <div>
    <review-form :movie="movie"></review-form>
    
    <ul>
      <review-list-item
        v-for="review of reviews" 
        :review="review" 
        :key="review.pk">
      </review-list-item>
    </ul>
    
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import ReviewForm from '@/components/ReviewForm.vue'

export default {
  name: 'ReviewList',
  components: { ReviewListItem, ReviewForm },
  props: { reviews: Array,
  movie: Object },
  
  created() {

  }
}
</script>

<style>

</style>