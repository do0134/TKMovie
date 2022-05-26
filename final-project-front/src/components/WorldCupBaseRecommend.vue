<template>
  <div>
    <router-link :to="{ name: 'moviedetail', params: { moviePk: movie.id } }">
      <div class="card m-3 " id="cardimg">    
        <img :src=" winnerPostPath" class="card-img-top" style="height: 400px; width: 295px;" alt="img">
          <div class="card-body">
            <h5 class="card-title fw-bold text-dark">{{movie.title}}</h5>
          </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'WorldCupBaseRecommend',
  props: {
    movie: Object,
  },

  computed: {
    winnerPostPath(){
      return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
    },
    winnerPk(){
      return this.movie.pk
    }
  },
  methods: {
    goMovie(movieId) {
      this.$router.push({ name: 'moviedetail', params: { moviePk: movieId } })
    }
  },
  created(){

  }
}
</script>

<style>
#cardimg img {
  transition: all 0.2s linear;
}
#cardimg:hover img {
  transform: scale(1.1);
}
</style>