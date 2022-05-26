<template>
<div class="container">
  <div class="row">
    <div class="col-12">
    <img :src="getBack" alt="backUrl" class = "backgroundImg">

    <img :src="posterUrl" alt=imgUrl class = "posterImg">
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
        this.backUrl = `https://image.tmdb.org/t/p/w500${res.data.backdrops[2].file_path}`
        
      })
      .catch(err=>
        console.log(err))
    }
  },
  computed:{
    getBack: function() {
      return this.backUrl
    }
  },
  created(){
    this.getPopularMovie()
  }

}
</script>

<style>
.backgroundImg{
  width : 100%;
  height : 100%;
  opacity: 0.3;
}
.posterImg{
  position: absolute;
  top:175px;
  left:80px;
}
</style>