<template>
  <div>
    <p>{{ a }}</p>
    <p>{{ b }}</p>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name : 'MovieWorldCupView',
  data(){
    return{
      sixteen_list : [],
      eight_list : [],
      four_list: [],
      final_list:[],
      a:{},
      b:{},
    }
  },
  computed : {
    ...mapGetters(['movieWorldcup'])
  },
  methods : {
    ...mapActions(['fetchMovieWorldCup',]),
    start(){
      this.sixteen_list = this.movieWorldcup
    },
    selectArgu(){
      if (this.sixteen_list.length > 0){
        this.a = this.sixteen_list[0]
        this.b = this.sixteen_list[1]
        this.sixteen_list.shift() 
        this.sixteen_list.shift() 
      } else if (this.eight_list.length > 0) {
        this.a = this.eight_list[0]
        this.b = this.eight_list[1]
        this.eight_list.shift() 
        this.eight_list.shift() 
      } else if (this.four_list.length >0){
        this.a = this.four_list[0]
        this.b = this.four_list[1]
        this.four_list.shift() 
        this.four_list.shift() 
      } else if (this.final_list.lengh>0){
        this.a = this.final_list[0]
        this.b = this.final_list[1]
        this.final_list.shift() 
        this.final_list.shift() 
      }
    },
    winner(){
      
    },
  },
  created(){
    this.fetchMovieWorldCup(),
    this.start(),
    this.selectArgu()
  }

}
</script>

<style>

</style>