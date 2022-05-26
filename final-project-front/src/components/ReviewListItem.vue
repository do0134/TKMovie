<template>
  <div>
    
    {{ review.content }}
    <div class="star-ratings">
      <div 
        class="star-ratings-fill space-x-2 text-lg"
        :style="{ width: ratingToPercent + '%' }"
      >
        <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
      </div>
      <div class="star-ratings-base space-x-2 text-lg">
        <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListItem',
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.pk,
        review: this.review.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    ratingToPercent() {
      const score = +this.review.rating * 20;
      return score + 1.5;}
  },
  
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.star-ratings {
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
 
.star-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
 
.star-ratings-base {
  z-index: 0;
  padding: 0;
}
</style>