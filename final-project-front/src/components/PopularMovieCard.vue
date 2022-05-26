<template>
  <div>    
    <!-- <div>
      <b-button v-b-modal.modal-scrollable>Show Modal</b-button>
      <b-modal id="modal-scrollable" scrollable title="Scrollable Content" ok-only>
        <p v-for="article in articles" :key="article.pk">{{  }}</p>
        <p @click="goProfile" id="a" class="ms-3 mt-2" style="cursor:pointer">{{  }}</p>
      </b-modal>
    </div> -->
    <!-- <div class="card m-3" id="cardimg" @click="goMovie(movie.id)">    
      <img :src="imgUrl" class="card-img-top" style="height: 400px; width: 295px;" alt="img">
        <div class="card-body">
          <h5 class="card-title fw-bold text-dark">{{movie.title}}</h5>
        </div>
    </div> -->
    <router-link :to="{ name: 'moviedetail', params: { moviePk: movie.id } }">    
      <div class="card m-3" id="cardimg">    
        <img :src="imgUrl" class="card-img-top" style="height: 400px; width: 295px;" alt="img">
          <div class="card-body">
            <h5 class="card-title fw-bold text-dark">{{movie.title}}</h5>
          </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "PopularMovieCard",
  props: {
    movie: Object,
  },
  data: function(){
    return {
      imgUrl:`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
      }
  },
  methods: {
    goMovie(movieId) {
      this.$router.push({ name: 'moviedetail', params: { moviePk: movieId } })
    }
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