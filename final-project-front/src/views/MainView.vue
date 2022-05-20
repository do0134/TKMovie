<template>
  <div>
    <nav-bar/>
    <br>
    <popular-movie-card />
  </div>  
</template>

<script>
import { mapState } from 'vuex';
import PopularMovieCard from '@/components/PopularMovieCard.vue';
import NavBar from '@/components/NavBar.vue'

export default {
  name : 'MainView',
  components : {
    PopularMovieCard,
    NavBar,
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

</style>