<template>
  <div class ="worldcupitem" @click="sendWinner">
    <img :src="`https://image.tmdb.org/t/p/w500${this.changeMovie.poster_path}`" alt=imgUrl>
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
</style>