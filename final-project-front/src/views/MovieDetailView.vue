<template>
  <div>
    {{ movie }}
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: "MovieDetailView",
  data() {
      return {
        moviePk: this.$route.params.moviePk
      }
    },
  computed : {
    ...mapGetters(['movie'])
  },
  methods : {
    ...mapActions(['fetchMovie',]),
  },
  created(){
    this.fetchMovie(this.moviePk)
  }
}
</script>

<style>

</style>