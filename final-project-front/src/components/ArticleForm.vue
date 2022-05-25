<template>
  <div class = 'container'>
    <div class = "row">
      <form @submit.prevent="onSubmit" class = "createForm col-12">
        <table class = "table table-bordered">
          <tbody>
            <tr>
              <th scope = "row" id="color" class="pt-4">
                제목
              </th>
              <td><input v-model="newArticle.title" class = "titleInput" type="text" id="title" placeholder="제목을 입력하세요." /></td>
            </tr>
            <tr>
              <th scope = "row" class="content pt-4" id="color">
                내용
              </th>
              <td><textarea v-model="newArticle.content" rows="10" cols="80" class = "contentInput" type="text" id="content" placeholder="내용을 입력하세요."></textarea></td>
            </tr>
          </tbody>
        </table>
        <div>
          <button class="btn btn-light" id="button">{{ action }}</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style>
#button { 
  /* text-decoration: none;
  color: black;
  border: 0; */
  box-shadow: none;
}
.createForm{
  display : flex;
  height : 786px;
  flex-direction: column;
}

.titleInput{
  width : 100%;
  border: 1px solid #ffffff;
  padding: 16px 14px;
  background: #fff;
}

.contentInput{
  width:100%;
  border: 1px solid #ffffff;
  padding: 16px 14px;
  background: #fff;
}
#color {
  background: rgb(253, 252, 226);
}
</style>
