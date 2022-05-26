<template>
  <span>{{ newCreatedAt }}</span>
</template>

<script>

export default {
  name : "ArticleListCreated",
  props : {
    article: Object,
  },
  data() {
    return{
      newCreatedAt: '',
      nowDate : '',
      nowMonth : ''
      }
  },
  methods : {
    newCreated: function(){
      const now = new Date()
      const nowYear = String(now.getFullYear())
      if (now.getMonth()< 9){
        this.nowMonth = '0'+String(now.getMonth()+1)
      } else{
        this.nowMonth = String(now.getMonth()+1)
      }
      console.log(this.nowMonth)
      if (now.getDate()<10){
        this.nowDate = '0'+String(now.getDate())
      } else {
        this.nowDate = String(now.getDate())
      }
      if (nowYear === this.article.created_at.slice(0,4) && this.nowMonth === this.article.created_at.slice(5,7) && this.nowDate === this.article.created_at.slice(8,10)){
        this.newCreatedAt = String(this.article.created_at.slice(11,12)+9)+String(this.article.created_at.slice(13,16))
        console.log('here')
        return this.newCreatedAt
      } else if(nowYear === this.article.created_at.slice(0,4)){
        this.newCreatedAt = this.article.created_at.slice(5,10)
        return this.newCreatedAt
      } else{
        this.newCreatedAt = this.article.created_at.slice(0,10)
        return this.newCreatedAt
      }
    }
  },
  created(){
    this.newCreated()
  }
}
</script>

<style>

</style>
