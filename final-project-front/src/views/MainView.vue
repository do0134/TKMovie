<template>
  <div class="bg-dark text-white">
    <h2>맨 위에 보여줄 영화는 어떤 영화인가?</h2>
    <br>
    
    <h2>PopularMovie (영화마다 datail 걸어주는 것 아직 안 함)</h2>

    <VueSlickCarousel v-bind="settings" :arrows="true" :dots="true" >
      <popular-movie-card v-for="movie in popularMovie" :key="movie.id" :movie="movie" />
    </VueSlickCarousel>

    <br>

    <h2>Now Playing Movie</h2>
    <VueSlickCarousel v-bind="settings" :arrows="true" :dots="true" >      
      <now-playing-movie-card v-for="movie in nowPlaying" :key="movie.id" :movie="movie"/>    
    </VueSlickCarousel>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import PopularMovieCard from '@/components/PopularMovieCard.vue';
import NowPlayingMovieCard from '@/components/NowPlayingMovieCard.vue';
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
// optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

export default {
  name : 'MainView',
  components : {
    PopularMovieCard,
    NowPlayingMovieCard,
    VueSlickCarousel
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
  computed:{
    ...mapState(['popularMovie']),
    ...mapState(['nowPlaying']),
  },
  methods : {
    getPopularMovie(){
      this.$store.dispatch('getPopularMovie')
    },
    getNowPlayingMovie(){
      this.$store.dispatch('getNowPlayingMovie')
    }
  },
  created(){
    this.getPopularMovie(),
    this.getNowPlayingMovie()
  }

}

</script>

<style>
  .wrapper {
    display: flex;
    overflow-x: auto;
  }
  .slick-prev:before {
  left : 0px;
  content: "<";
  color: red;
  font-size: 30px;
  }
  .slick-next {
    right : 0px;
    content: ">";
    color: red;
    font-size: 30px;
    background-color : black;
  }
  .slick-list {
    margin : 5px;
  }
  data-v-e4caeaf8{
    display : none;
  }
  data-v-e4caeaf8{
    display : none;
  }
  /* 옆으로 컨트롤 하는 거(carousel로 하든가 다시 생각)
  .wrapper::-webkit-scrollbar {
    width: 0;
  } */
</style>