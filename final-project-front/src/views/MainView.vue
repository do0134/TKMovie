<template>
  <div class="bg-black text-white">
    <h2>맨 위에 보여줄 영화는 어떤 영화인가?</h2>
    <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="10000">
          <img src="#" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item" data-bs-interval="2000">
          <img src="#" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="#" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <br>
    
    <h2>PopularMovie (영화마다 datail 걸어주는 것 아직 안 함)</h2>

    <VueSlickCarousel v-bind="settings" :arrows="true" >
      <popular-movie-card v-for="movie in popularMovie" :key="movie.id" :movie="movie" />
    </VueSlickCarousel>

    <br>

    <h2>Now Playing Movie</h2>
    <VueSlickCarousel  v-bind="settings" :arrows="true" >      
      <now-playing-movie-card v-for="movie in nowPlaying" :key="movie.id" :movie="movie"/>    
    </VueSlickCarousel>

    <h2>{{ currentUser.username }}님 취향 저격 영화</h2>
    <world-cup-base-list v-if="!winner.length===0" :movie="winner"/>
    <router-link v-else :to="{ name: 'movieworldcup'}"> <button  class="btn btn-primary"> 이상형 월드컵을 해보세요 </button> </router-link>
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
        }

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


    // getCarouselMovie() {
    //   this.carouselMovie = _.sortBy(this.nowPlaying, 'vote_average')
    // }
  },
  created(){
    this.getPopularMovie(),
    this.getNowPlayingMovie(),
    this.fetchWinner(this.currentUser.username)


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