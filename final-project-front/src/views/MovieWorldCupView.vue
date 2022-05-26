<template>
  <div class = "worldcup">
    <div class="indexDiv">
      {{ username }}님의 취향저격 영화 월드컵 {{ checkmatch }} {{ totalIndex }}
    </div>
    
    
    <movie-world-cup 
    v-if="!checkFinish"
    :movie="reA"
    @send-winner="win" />

    <movie-world-cup 
    v-if="!checkFinish"
    :movie="reB" 
    @send-winner="win" />
    <movie-worldcup-winner 
    v-else
    :movie="sendWinner"
    />
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

import MovieWorldCup from '../components/MovieWorldCup.vue'
import MovieWorldcupWinner from '@/components/MovieWorldcupWinner.vue'


export default {
  name : 'MovieWorldCupView',
  components: { MovieWorldCup, MovieWorldcupWinner },
  data(){
    return{
      sixteen_list : [],
      eight_list : [],
      four_list: [],
      final_list:[],
      a:{},
      b:{},
      isSixteen: false,
      isEight: false,
      isFour: false,
      smallIdx : 1,
      bigIdx: 8,
      isFinal:false,
      moviePk: 0,
      isFinish: false,
      winner: {},
    }
  },
  computed : {
    ...mapGetters(['movieWorldcup','currentUser']),
    totalIndex(){ if (this.thisFinal){
        return 
        } else{
          return `${this.smallIndex} / ${this.bigIndex}`
        }
    },
    thisFinal(){
      return this.isFinal
    },
    smallIndex(){
      return this.smallIdx
    },
    bigIndex(){
      return this.bigIdx
    },
    username(){
      return this.currentUser.username
    },
    reA(){
      return this.a
    },
    reB(){
      return this.b
    },
    check_sixteen(){
      return this.sixteen_list
    },
    sixteenFin(){
      return this.isSixteen
    },
    check_eight(){
      return this.eight_list
    },
    eightFin(){
      return this.isEight
    },
    check_four(){
      return this.four_list
    },
    fourFin(){
      return this.isFour
    },
    checkmatch(){
      if (!this.sixteenFin){
        return '16강'
      } else if (!this.eightFin){
        return '8강'
      } else if (!this.fourFin){
        return '4강'
      } else{
        return '결승'
      }
    },
    movieKey(){
      return this.moviePk
    },
    checkFinish(){
      return this.isFinish
    },
    sendWinner(){
      return this.winner
    }
  },
  methods : {
    ...mapActions(['fetchMovieWorldCup','worldcupWin']),
    start(){
      this.sixteen_list = this.movieWorldcup
    },
    selectArgu(){
        this.a = this.sixteen_list[0]
        this.b = this.sixteen_list[1]
        this.sixteen_list.shift() 
        this.sixteen_list.shift()
        return this.a, this.b
      },
     
    win: function(inputData){
      let movie = inputData
      console.log(movie)
       if (this.check_sixteen.length > 0){
         this.eight_list.push(movie)
         this.smallIdx++
         this.a = this.sixteen_list[0]
         this.b = this.sixteen_list[1]

        this.sixteen_list.shift() 
        this.sixteen_list.shift()}
       else if (this.check_sixteen.length ===0 && !this.sixteenFin){
         this.isSixteen = true
         this.bigIdx = 4
         this.smallIdx = 1
         this.eight_list.push(movie)
         this.a = this.eight_list[0]
         this.b = this.eight_list[1]
         this.eight_list.shift()
         this.eight_list.shift()
         
       }
       
       else if (this.check_eight.length > 0) {
         this.four_list.push(movie)
         this.smallIdx++
         this.a = this.eight_list[0]
         this.b = this.eight_list[1]
         this.eight_list.shift() 
         this.eight_list.shift()

       } 

       else if (this.check_eight.length ===0 && !this.eightFin){
         this.isEight = true
         this.four_list.push(movie)
         this.bigIdx = 2
         this.smallIdx = 1
         this.a = this.four_list[0]
         this.b = this.four_list[1]
         this.four_list.shift()
         this.four_list.shift()
       }
       
       else if (this.check_four.length > 0) {
         this.final_list.push(movie)
         this.smallIdx++
         this.a = this.four_list[0]
         this.b = this.four_list[1]
         this.four_list.shift()
         this.four_list.shift()
       }  
       else if (this.check_four.length === 0 && !this.fourFin){
         this.bigIdx = ''
         this.smallIdx = ''
         this.isFour = true
         this.final_list.push(movie)
         this.a = this.final_list[0]
         this.b = this.final_list[1]
         this.final_list.shift()
         this.final_list.shift()
         this.isFinal = true
       }
       else  {
         this.isFinish = true
         this.winner = movie
         this.moviePk = movie.pk
         this.worldcupWin(this.movieKey)
         console.log('chickendinner')
       }
    },
    test(){
      console.log(123)
    }},

  created(){
    this.fetchMovieWorldCup(),
    this.start(),
    this.selectArgu()
  }

}
</script>

<style>
.indexDiv{
  height: 72px;
  display:flex;
  width: 100%;
  align-items: center;
  justify-content: center;
  background-color : rgba( 0, 0, 0, 0.5 );
  color: white;
}
.worldcup{
  background-color: #181818;
  height: 22.525em;
  font-size: calc(2 * (1vw + 1vh - 1vmin));
  font-family: open sans,helvetica neue,Helvetica,Arial,sans-serif;
}
</style>