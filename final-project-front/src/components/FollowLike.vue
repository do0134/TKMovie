<template>
  <div>
    <VueSlickCarousel v-bind="settings" :arrows="true">
      <follow-like-item v-for="movie in followerLike" :movie="movie" :key="movie.pk"/>
    </VueSlickCarousel>
    
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'


import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
// optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
import FollowLikeItem from './FollowLikeItem.vue'

export default {
  components: { VueSlickCarousel,FollowLikeItem },
  name: 'FollowLike',
  data(){
    return {
      settings: {
        "focusOnSelect": true,
        "infinite": true,
        "speed": 500,
        "slidesToShow": 3,
        "slidesToScroll": 3,
        "touchThreshold": 5,
        "variableWidth": true
        },
        userPk: this.$route.params.userPk
    }
  },
  methods:{
    ...mapActions(['fetchFollowerLike'])
  },
  computed:{
    ...mapGetters(['followerLike','currentUser'])
  },
  created(){
    console.log(this.followerLike)
    this.fetchFollowerLike(this.currentUser.pk)
  }
}
</script>

<style>

</style>