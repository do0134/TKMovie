<template>
  <div class="my-5 container d-flex">
    <img :src="`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`" alt="" style="height: 500px">
    <div class="mx-5">
      <div class="d-flex justify-content-between">
        <div>
          <h2 class="d-flex">{{ movie.title }}</h2>
          <p class="d-flex ms-1">개봉일 {{ movie.released_date }}</p>
        </div>
        <div>
          <b-button @click="[likeMovie(moviePk)]" variant="link" id="link" class="mt-2">
            <b-icon v-if="changeLike===false" icon="heart" aria-hidden="true" variant="danger"></b-icon>
            <b-icon v-else icon="heart-fill" aria-hidden="true" variant="danger"></b-icon>
            <p class="mt-2">{{ likeCount }}명이 이 영화를 좋아합니다</p>
          </b-button>
        </div>
      </div>
      <hr class="my-0">
      <p class="d-flex ms-2 mt-3">평점 {{ movie.vote_avg }}</p>
      <p>장르:
        <span v-for="genre in movie.genres" :key="genre.id">{{genre.name}} |</span>
      </p>
      <p>줄거리{{ movie.overview }}</p>
      
      <b-button class="mt-2" variant="link" :to="{ name: 'main' }" id="link">
        <i class="fa-solid fa-house"></i>
      </b-button>
    </div>
    <review-list :reviews="movie.movie_review" :movie="movie"></review-list>
  </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import ReviewList from '@/components/ReviewList.vue'

export default {
  name: "MovieDetailView",
  components: { ReviewList },
  data() {
      return {
        moviePk: this.$route.params.moviePk,
        // imgUrl:`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
      }
    },
  computed : {
    ...mapGetters(['movie','currentUser']),
    changeLike(){
      return this.checkLike()
    },
    likeCount(){
      return this.movie.movie_like.length
    }
  },
  methods : {
    ...mapActions(['fetchMovie', 'likeMovie']),
    checkLike(){
        for (let i of this.movie.movie_like){
          if (i === this.currentUser.pk){
            return true
          } 
        } return false
        },
  },
  created() {
    this.fetchMovie(this.moviePk),
    this.checkLike()

  }
}
</script>

<style>

</style>