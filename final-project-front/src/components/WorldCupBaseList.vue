<template>
  
  <VueSlickCarousel v-bind="settings" :arrows="true">
    <world-cup-base-recommend v-for="movie in worldcupBase" :key="movie.pk" :movie="movie" />
  </VueSlickCarousel>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
// optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
import { mapActions, mapGetters } from 'vuex'
import WorldCupBaseRecommend from './WorldCupBaseRecommend.vue'

export default {
  name : 'WorldCupBaseList',
  components : {
    WorldCupBaseRecommend,
    VueSlickCarousel,
  },
  props: {
    movie: Object,
  },
  data() {
    return {
      settings: {
        "focusOnSelect": true,
        "infinite": true,
        "speed": 500,
        "slidesToShow": 3,
        "slidesToScroll": 3,
        "touchThreshold": 5,
        "variableWidth": true
        }

  }},
  computed : {
    ...mapGetters(['worldcupBase'])
  },
  methods : {
    ...mapActions(['getWorldcupBase'])
  },
  created(){
    this.getWorldcupBase(this.movie.pk),
    console.log(this.movie)
  }
}
</script>

<style>

</style>