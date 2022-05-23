<template>
  <div>
    <div class="card m-3 " id="cardimg">    
      <img :src="imgUrl" class="card-img-top" style="height: 400px; width: 295px;" alt="img">
        <div class="card-body">
          <h5 class="card-title fw-bold">{{movie.title}}</h5>
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
#cardimg img {
  transition: all 0.2s linear;
}
#cardimg:hover img {
  transform: scale(1.1);
}
</style>