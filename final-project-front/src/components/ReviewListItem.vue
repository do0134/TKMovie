<template>
  <div>
    <div class="d-flex">
      {{ currentUser.username }}
      <div class="ms-3">
        <span v-if="checkEdit">
          <input type="text" v-model="payload.content">
          <input type="number" name="points" min="0" max="5" step="1" v-model="payload.rating">
          <button @click="onUpdate" class="btn-sm btn btn-link" id="link">
            <b-icon icon="check-lg" variant="dark" class="me-1"></b-icon></button> |
          <button @click="switchIsEditing" class="btn-sm btn btn-link" id="link">
            <b-icon icon="x-lg" variant="dark" class="me-1"></b-icon></button>
        </span>
        <span v-if="currentUser.pk === review.user && !checkEdit">
          <button @click="switchIsEditing" class="btn-sm btn btn-link" id="link">
            <b-icon icon="pencil-square" aria-hidden="true" variant="dark"></b-icon></button> |
          <button @click="deleteReview(payload)" class="btn-sm btn btn-link" id="link">
            <b-icon icon="trash" aria-hidden="true" variant="dark"></b-icon></button>
        </span>
      </div>
    </div>

    <div class="d-flex my-2">
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
      <div>
        <span v-if="!checkEdit" class="ms-5">
          <b-icon icon="chat-square-quote-fill" variant="warning" class="me-1"></b-icon>{{ payload.content }}</span>      
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
        content: this.review.content,
        rating: this.review.rating,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    ratingToPercent() {
      const score = +this.review.rating * 20;
      return score + 1.5;},
    checkEdit(){
      return this.isEditing
    }
  },
  
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    },

  },
  created(){
    console.log(this.review)
    console.log(this.review.user)

  }

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