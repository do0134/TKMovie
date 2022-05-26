import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    movieWorldcup: [],
    movie: {},
    winner:{},
    topTen:[],
    followerLike: [],
  },

  getters: {
    movieWorldcup: state => state.movieWorldcup,
    movie: state => state.movie,
    winner: state => state.winner, 
    topTen: state => state.topTen,
    followerLike: state => state.followerLike
  },

  mutations: {
    SET_MOVIE_WORLDCUP: (state, movieWorldcup) => state.movieWorldcup = movieWorldcup,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.movie_review = reviews),
    SET_WINNER: (state,winner) => state.winner = winner,
    SET_WORLDCUPBASE: (state, worldcupBase) => state.worldcupBase = worldcupBase,
    SET_TOPTEN: (state, topTen) => state.topTen = topTen,
    SET_FOLLOWERLIKE: (state,followerLike) => state.followerLike = followerLike
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

    fetchWinner({ commit,getters }, username){
      axios({
        url: drf.movies.setWinner(username),
        method: 'get',
        headers: getters.authHeader,
      }) .then( res => {
        commit('SET_WINNER', res.data)
      }).catch(err => console.log(err.response))
      
    },

    fetchTopTen({ commit, getters }) {
      axios({
        url: drf.movies.topTen(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_TOPTEN', res.data)
        })
        .catch(err => console.error(err.response))
    },

    fetchFollowerLike({ commit, getters }, userPk) {

      axios({
        url: drf.movies.followerLike(userPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_FOLLOWERLIKE', res.data)
        })
        .catch(err => console.error(err.response))
    },

    likeMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.likeMovie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(res => { 
        commit('SET_MOVIE', res.data) 
      })
      .catch(err => console.error(err.response))
    },
    createReview({ commit, getters }, { moviePk, content, rating }) {
      const review = { content, rating }
      axios({
        url: drf.movies.reviews(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader
      })
        .then(res => {
          console.log(res.data)
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },
    updateReview({ commit, getters }, { moviePk, reviewPk, content, rating }) {
      const review = { content, rating }
      console.log(moviePk)
      axios({
        url: drf.movies.review(moviePk, reviewPk),
        method: 'put',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(1234567)
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteReview({ commit, getters }, { moviePk, reviewPk }) {

        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.movies.review(moviePk, reviewPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_MOVIE_REVIEWS', res.data)
            })
            .catch(err => console.error(err.response))
        }
    },
    worldcupWin({ commit,getters }, moviePk) {

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
