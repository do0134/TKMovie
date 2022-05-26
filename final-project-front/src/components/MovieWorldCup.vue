<template>
  <div class ="worldcupitem" @click="sendWinner">
    <img :src="`https://image.tmdb.org/t/p/w500${this.changeMovie.poster_path}`" alt=imgUrl>
    <div class ="worldcupcontent">
      <h2 class ="come d-flex ms-1" style="font-size:25px;">{{ movie.title }}</h2>
      <hr>
      <div class ="d-flex justify-content-between mx-1">
        <p style="font-size:20px;">개봉일 {{ movie.released_date }}</p>
        <p style="font-size:20px;">평점 {{ movie.vote_avg }}</p>
      </div>
      <p style="font-size:20px;">{{ movie.overview }}</p>
    </div>
  </div>
</template>

<script>


export default {
  name : 'MovieWorldCup',
  props:{
    movie:Object
  },
  computed: {
    changeMovie(){
      return this.movie
    }
  },
  data(){
    return {
      imgUrl:`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`,
      sendData : {}
      }
  },
  methods: {
    test(){
      console.log(123)
    },
    sendWinner(){
      this.sendData = this.changeMovie
      console.log(this.sendData)
      this.$emit('send-winner', this.sendData)
    }
  }


}
</script>

<style>
.worldcupitem{
  display: inline-block;
  width : 50%;
}
.worldcupitem img {
  transition: all 0.2s linear;
  transition-property: background-color;
  transition-duration: 1s;
  transition-timing-function: ease-out;
}
.worldcupitem:hover img {
  filter: brightness(20%);
}
.worldcupcontent {
  cursor: pointer;
  position: absolute;
  top: 300px;
  color: white;
  opacity:0;
  transition:0.5s all;
  width: 25%;
  margin-left: 12.5%;
}
.worldcupitem:hover .worldcupcontent {
  opacity:1;
}

</style>
