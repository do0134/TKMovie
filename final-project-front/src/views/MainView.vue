<template>
  <popular-movie-card />
</template>

<script>
import { mapState } from 'vuex';
import PopularMovieCard from '@/components/PopularMovieCard.vue';

export default {
  name : 'MainView',
  components : {
    PopularMovieCard,
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