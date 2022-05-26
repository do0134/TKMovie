<template>
  <div>    
  <div class="card m-3" id="cardimg">    
    <img :src="imgUrl" class="card-img-top" style="height: 400px; width: 295px;" alt="img">
    <div class="title">
      <span class="more" @click="goMovie(movie.id)" style="cursor:pointer">{{movie.title}}</span>
    </div>
    
  </div>
</div>
</template>

<script>
export default {
  name: "NowPlayingMovieCard",
  props :{
    movie : Object
  },
  data: function(){
    return {
      imgUrl:`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`,
      }
  },
}
</script>

<style>

</style>