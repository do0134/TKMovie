<template>
<div>
  <div :src="getBack" alt=backUrl class = "backgroundImg" :style="backUrl"></div>
  <div class = "wrapper">
    <img :src="posterUrl" alt=imgUrl class = "posterImg">
    <div class="content mt-5 ms-5 winner-title">
      <div class="d-flex justify-content-between">
        <h2 class = "d-flex" style="font-size:40px;">
          <b-icon icon="camera-reels" animation="fade" font-scale="1" class="me-3"></b-icon>{{ titleC }}</h2>
        <p class = "d-flex mt-4" style="font-size:20px;">개봉<span class="mx-2"></span>{{ releasedDate }}</p>
      </div>
      <hr class = "my-0">
      <span class = "mt-3 vote" style="font-size:20px;">평점<span class="mx-2"></span>{{ voteAvg }}</span>
      <span class = "" style="font-size:25px;">{{ genres }}(시리얼라이저 고치고 넣기!!)</span>
      <!-- <p class = "winner-title"><span v-for="genre in genres" :key="genre.id">{{genre.name}}</span></p> -->
      <p class = "mt-4" style="font-size:25px;">{{ overviewC }}</p>
      <p @click="goDetail()" class="mb-0 d-flex justify-content-end" style="cursor:pointer; font-weight:bold; font-color:white; font-size:25px;">
        <b-icon icon="pencil-square" aria-hidden="true" variant="white" class="me-2"></b-icon> 리뷰 작성하기</p>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'

const API_URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = "38fb6be42c82ed986f17fb3d9195b8bc"


export default {
  name: 'MovieWorldcupWinner',
  props:{
    movie : Object,
  },
  data(){
    return {
      posterUrl:`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`,
      backUrl: '',
      title: '',
      overview: '',
      vote_avg: '',
      genres: '',
      released_date:''
    }
  },
  methods : {
    getPopularMovie(){
      const GET_IMAGE = `${this.movie.id}/images`
      const params = {
        api_key : API_KEY,
      }
      axios({
        method:'get',
        url: API_URL+GET_IMAGE,
        params : params
      })
      .then(res=>{
        this.backUrl = `background-image: url(https://image.tmdb.org/t/p/w500${res.data.backdrops[2].file_path})`
        
      })
      .catch(err=>
        console.log(err))
    },
    getTitle(){
      this.title = this.movie.title,
      this.overview = this.movie.overview,
      this.vote_avg = this.movie.vote_avg
      this.genres = this.movie.genres
      this.released_date = this.movie.released_date
    },
    goDetail() {
        this.$router.push({ name: 'moviedetail', params: { moviePk: this.movie.id } })
    }
  },
  computed:{
    getBack: function() {
      return this.backUrl
    },
    titleC(){
      return this.title
    },
    overviewC(){
      return this.overview
    },
    voteAvg() {
      return this.vote_avg
    },
    genresC() {
      return this.genres
    },
    releasedDate() {
      return this.released_date
    }
  },
  created(){
    this.getPopularMovie(),
    this.getTitle()
  }

}
</script>

<style>
.backgroundImg {
  width: 100%;
  height: 100vh;
  opacity: 0.3;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}
.wrapper {
  width: 80%;
  position: absolute;
  top:20vh;
  left:10vw;
}
.posterImg{
  max-width: 100%;
  height: auto;
}
.winner-title{
  color: white;
}
.vote {
  left: 10vw;
}
</style>