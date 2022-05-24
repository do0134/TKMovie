<template>
  <div>
    
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name : 'MovieWorldCupView',
  data(){
    
  },
  computed : {
    ...mapGetters(['movieWorldcup'])
  },
  methods : {
    ...mapActions(['fetchMovieWorldCup',]),

  },
  created(){
    this.fetchMovieWorldCup()
  }

}
</script>

<style>

</style>