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
      newCreatedAt: ''
      }
  },
  methods : {
    newCreated: function(){
      const now = new Date()
      const nowYear = String(now.getFullYear())
      const nowMonth = String(now.getMonth()+1)
      const nowDate = String(now.getDate())
      if (nowYear === this.article.created_at.slice(0,4) && nowMonth === this.article.created_at.slice(6,7) && nowDate === this.article.created_at.slice(8,10)){
        this.newCreatedAt = this.article.created_at.slice(11,16)
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