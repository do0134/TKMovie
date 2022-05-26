<template>
<div>
  <div :src="getBack" alt=backUrl class = "backgroundImg" :style="backUrl"></div>
  <div class = "wrapper">
    <img :src="posterUrl" alt=imgUrl class = "posterImg">
    <div class="content mt-5 ms-5">
      <h2 class = "winner-title">{{ titleC }}</h2>
      <button class="btn btn-white">
        <router-link :to="{ name: 'moviedetail', params: { moviePk: movie.pk } }"> 
          리뷰 쓰러 가기
        </router-link></button>
    </div>
  </div>
  <!-- <div class="content">
    <h2 class = "winner-title">{{ titleC }}</h2>
    <button class="btn btn-primary">
      <router-link :to="{ name: 'moviedetail', params: { moviePk: movie.pk } }"> 
        리뷰 쓰러 가기
      </router-link></button>
  </div> -->
</div>
<!-- <div class="container">
  <div class="row">
    <div class="col-12">
      <img :src="getBack" alt="backUrl" class = "backgroundImg">
      <img :src="posterUrl" alt=imgUrl class = "posterImg">
      <h2 class = "winner-title">{{ titleC }}</h2>
      <button class="btn btn-primary">
        <router-link :to="{ name: 'moviedetail', params: { moviePk: movie.pk } }"> 
          리뷰 쓰러 가기
        </router-link></button> 
    </div>
  </div>
</div> -->
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
    }
  },
  methods : {
    getPopularMovie(){
      const GET_IMAGE = `${this.movie.pk}/images`
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
      this.overview = this.movie.overview
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
  width: 100%;
  position: absolute;
  top:20vh;
  left:20vw;
}
.posterImg{
  max-width: 100%;
  height: auto;
}
/* .content {
  position: absolute;
  top:200px;
  right:200px;
} */
/* .backgroundImg{
  width : 1600px;
  height : 775px;
  opacity: 0.3;
  display: flex;
  justify-content: center;
} */

.winner-title{
  color: white;
}
/* .winner-overview{
  color:white;
  position: absolute;

} */
</style>