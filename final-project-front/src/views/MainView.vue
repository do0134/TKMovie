<template>
  <div class="bg-black text-white">
    <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="560"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Text slides with image -->
      <b-carousel-slide
        img-src="https://ifh.cc/g/3Tmfca.jpg"
      >
      </b-carousel-slide>

      <!-- Slides with custom text -->
      <b-carousel-slide img-src="https://ifh.cc/g/jjHQAT.png">

      </b-carousel-slide>

      <!-- Slides with image only -->
      <b-carousel-slide img-src="https://ifh.cc/g/165RrQ.jpg"></b-carousel-slide>

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
      <b-carousel-slide img-src="https://ifh.cc/g/tzm3dp.jpg"></b-carousel-slide>

      <!-- Slide with blank fluid image to maintain slide aspect ratio -->

    </b-carousel>

  </div>
    <br>
    
    <h2>PopularMovie</h2>
    <div class = "popular">
      <VueSlickCarousel v-bind="settings" :arrows="true" @init="onInitCarousel">
        <popular-movie-card v-for="movie in popularMovie" :key="movie.id" :movie="movie" />
      </VueSlickCarousel>
    </div>
    <br>
    
    <h2>Now Playing Movie</h2>
    <div class="popular">
      <VueSlickCarousel  v-bind="settings" :arrows="true" >      
        <now-playing-movie-card v-for="movie in nowPlaying" :key="movie.id" :movie="movie"/>    
      </VueSlickCarousel>
    </div>
    <h2 v-if="currentUser.pk>0">{{ currentUser.username }}님 취향 저격 영화</h2>
    <div class="popular">
      <router-link v-if="currentUser.pk>0 && !winner" :to="{ name: 'movie_worldcup'}"> <button  class="btn btn-primary"> 이상형 월드컵을 해보세요 </button> </router-link>
    
      <world-cup-base-list v-else :movie="winner"/>
    </div>
  </div>
</template>

<script>
import { mapState,mapActions,mapGetters } from 'vuex';
import PopularMovieCard from '@/components/PopularMovieCard.vue';
import NowPlayingMovieCard from '@/components/NowPlayingMovieCard.vue';
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
// optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

import WorldCupBaseList from '../components/WorldCupBaseList.vue'

export default {
  name : 'MainView',
  components : {
    PopularMovieCard,
    NowPlayingMovieCard,
    VueSlickCarousel,
    WorldCupBaseList
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
        },
        slide: 0,
        sliding: null,
        fPk: 526896,

      // carouselMovie: [],
      // imgUrl: []
  }},
  computed:{
    ...mapState(['popularMovie']),
    ...mapState(['nowPlaying']),
    ...mapGetters(['currentUser','winner']),


  },
  methods : {
    getPopularMovie(){
      this.$store.dispatch('getPopularMovie')
    },
    getNowPlayingMovie(){
      this.$store.dispatch('getNowPlayingMovie')
    },
    ...mapActions(['fetchWinner']),
    onSlideStart() {
        this.sliding = true
      },
      onSlideEnd() {
        this.sliding = false
      }


    // getCarouselMovie() {
    //   this.carouselMovie = _.sortBy(this.nowPlaying, 'vote_average')
    // }
  },
  created(){
    this.getPopularMovie(),
    this.getNowPlayingMovie(),
    this.fetchWinner(this.currentUser.username),
    console.log(this.winner)


    // console.log(this.carouselMovie)
    // this.getCarouselMovie()
  }

}

</script>

<style>
  .wrapper {
    display: flex;
    overflow-x: auto;
  }
  .slick-prev::before {
  left : 0px;

  color: white;
  font-size: 30px;
  }
  .slick-next::before {
    right : 0px;
    color: white;
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
  .carousel-item {
    display:flex;
    justify-content: center;
  }
  .carousel-inner{
    height: 540px;
    width: 100%;

  }
  .d-block{
    height:540px;
    width: 100%;
  }
  /* 옆으로 컨트롤 하는 거(carousel로 하든가 다시 생각)
  .wrapper::-webkit-scrollbar {
    width: 0;
  } */
  .goDetail1{
    position:absolute;
    bottom: 550px;
    left: 0px;
    width: 200px;
    height : 50px;
    
  }
  .popular{
    width: 1800px;
    margin-left:40px;
    
  }
</style>