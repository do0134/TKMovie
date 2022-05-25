import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    movieWorldcup: [],
    movie: {},

  },

  getters: {
    movieWorldcup: state => state.movieWorldcup,
    movie: state => state.movie,
  },

  mutations: {
    SET_MOVIE_WORLDCUP: (state, movieWorldcup) => state.movieWorldcup = movieWorldcup,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.reviews = reviews),
  },
  actions: {
    fetchMovieWorldCup({ commit, getters }) {
      axios({
        url: drf.movies.movieWorldcup(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_WORLDCUP', res.data)
        })
        .catch(err => console.error(err.response))
    },
    
    fetchMovie({ commit, getters }, moviePk) {
      console.log(moviePk)
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    worldcupWin({ commit,getters }, moviePk) {
      console.log(moviePk)
      axios({
        url: drf.movies.getWorldcupWinner(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_MOVIE',res.data))
      .catch(err => console.error(err.response))
    },


  }
}
