<template>
  <div>
    <h2>맨 위에 보여줄 영화는 어떤 영화인가?</h2>
    <br>
    
    <h2>PopularMovie (영화마다 datail 걸어주는 것 아직 안 함)</h2>
    <div class="wrapper">        
      <popular-movie-card v-for="movie in popularMovie" :key="movie.id" :movie="movie"/>    
    </div>
    <br>

    <h2>Now Playing Movie</h2>
    <now-playing-movie-card/>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import PopularMovieCard from '@/components/PopularMovieCard.vue';
import NowPlayingMovieCard from '@/components/NowPlayingMovieCard.vue';

export default {
  name : 'MainView',
  components : {
    PopularMovieCard,
    NowPlayingMovieCard,
  },
  computed:{
    ...mapState(['popularMovie']),
    ...mapState(['nowPlaying']),
  },
  methods : {
    getPopularMovie(){
      this.$store.dispatch('getPopularMovie')
    },
    getNowPlayingMovie(){
      this.$store.dispatch('getNowPlayingMovie')
    }
  },
  created(){
    this.getPopularMovie(),
    this.getNowPlayingMovie()
  }

}
</script>

<style>
  .wrapper {
    display: flex;
    overflow-x: auto;
  }

  /* 옆으로 컨트롤 하는 거(carousel로 하든가 다시 생각)
  .wrapper::-webkit-scrollbar {
    width: 0;
  } */
</style>