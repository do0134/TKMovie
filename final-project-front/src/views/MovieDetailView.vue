<template>
  <div class="my-5 container d-flex">
    <img :src="`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`" alt="" style="height: 500px">
    <div class="mx-5">
      <h2 class="d-flex">{{ movie.title }}</h2>
      <p class="d-flex mx-3">{{ movie.released_date }}</p>
      <b-button @click="[likeMovie(moviePk)]" variant="link" id="link">
        
        <b-icon icon="heart" aria-hidden="true" variant="danger"></b-icon>
      </b-button>
      <hr>
      <p>{{ movie.vote_avg }}</p>
      <p>{{ movie.genres }}</p>
      <p>장르
        <span v-for="genre in movie.genres" :key="genre.id">{{genre.name}}</span>
      </p>
      <p>줄거리{{ movie.overview }}</p>
      
      <b-button class="mt-2" variant="link" :to="{ name: 'main' }" id="link">
        <i class="fa-solid fa-house"></i>
      </b-button>
    </div>
  </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: "MovieDetailView",
  data() {
      return {
        moviePk: this.$route.params.moviePk,
        // imgUrl:`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
      }
    },
  computed : {
    ...mapGetters(['movie']),
    changeLike(){
      return this.checkLike()
    }
  },
  methods : {
    ...mapActions(['fetchMovie', 'likeMovie']),
  },
  created() {
    this.fetchMovie(this.moviePk)
  }
}
</script>

<style>

</style>