<template>
  <div class="comment-list mt-4">
    <comment-form class="px-5"></comment-form>
    <ul class="px-5">
      <comment-list-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk">
      </comment-list-item>        
    </ul>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentForm from '@/components/CommentForm.vue'

export default {
  name: 'CommentList',
  components: { CommentForm, CommentListItem },
  props: { comments: Array },
}
</script>

<style>
</style>