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
  name: 'FollowLikeItem',
  props:{
    movie:Object
  },
  data(){
    return{
      imgUrl:`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
    }
  },
  methods: {
    goMovie(movieId) {
      this.$router.push({ name: 'moviedetail', params: { moviePk: movieId } })
    }
  }
}
</script>

<style>
#cardimg img {
  transition: all 0.2s linear;
  transition-property: background-color;
  /*변형 완료 1초*/
  transition-duration: 1s;
  /*빠른 시작 서서히 감속*/
  transition-timing-function: ease-out;
}
#cardimg:hover img {
  transform: scale(1.1);
  filter: brightness(50%);
  background: rgba(255, 255, 255, 0.3);
}
#cardimg {
  text-align:center;
}
.title {
  line-height:1; 
  position:absolute; 
  left:50%; 
  transform:translateX(-50%); 
  top:200px; 
  height:120px; 
  transition:0.5s all
}
.more {
  display:block; 
  font-size:18x; 
  color:#fff; 
  background:rgb(0, 0, 0); 
  line-height:40px; 
  width:200px; 
  margin-top:30px; 
  opacity:0; 
  transition:0.5s all
}
#cardimg:hover .more {
  opacity:1;
  top:150px;
}
#cardimg:hover .title {
  top:150px;
}
</style>
