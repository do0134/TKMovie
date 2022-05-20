import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = "https://api.themoviedb.org/3"
const API_KEY = "38fb6be42c82ed986f17fb3d9195b8bc"
const popMovie = "/movie/popular/"
const nowPlaying = "/movie/now_playing/"

export default new Vuex.Store({
  state: {
    nowPlaying : [],
    popularMovie : [],
  },
  getters: {

  },
  mutations: {
    GET_POPULAR_MOVIE(state,  moviesData){
      state.popularMovie = moviesData
    },
    GET_NOWPLAYING_MOVIE(state,  moviesData){
      state.nowPlaying = moviesData
    },
  },
  actions: {
    getPopularMovie({commit}){
      const params = {
        api_key : API_KEY,
        language : 'ko-kr',
      }
      axios({
        method:'get',
        url: API_URL+popMovie,
        params : params
      })
      .then(res=>{
        const moviesData = res.data.results
        console.log(moviesData)
        commit('GET_POPULAR_MOVIE', moviesData)
      })
      .catch(err=>
        console.log(err))
    },
    getNowPlayingMovie({commit}){
      const params = {
        api_key : API_KEY,
        language : 'ko-kr'
      }
      axios({
        method : 'get',
        url : API_URL+nowPlaying,
        params : params
      })
      .then(res =>{
        const moviesData = res.data.results
        console.log(moviesData)
        commit('GET_NOWPLAING_MOVIE',moviesData)
      })
      .catch(err=>
        console.log(err))
    }
  },
  modules: {
  }
})
