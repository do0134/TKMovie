<template>
  <div>
    <ul>
      <review-list-item
        v-for="review in reviews" 
        :review="review" 
        :key="review.pk">
      </review-list-item>
    </ul>
    <review-form></review-form>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import ReviewForm from '@/components/ReviewForm.vue'

export default {
  name: 'ReviewList',
  components: { ReviewListItem, ReviewForm },
  props: { reviews: Array }
}
</script>

<style>

</style>