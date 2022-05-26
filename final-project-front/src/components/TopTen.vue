<template>
  <div>
    <top-ten-item v-for="movie in topTen" :movie="movie" :key="movie.pk"/>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import TopTenItem from './TopTenItem.vue'
export default {
  components: { TopTenItem },
  name: 'TopTen',
  methods:{
    ...mapActions(['fetchTopTen'])
  },
  computed:{
    ...mapGetters(['topTen'])
  },
  created(){
    this.fetchTopTen()
  }
}
</script>

<style>

</style>