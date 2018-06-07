<style scoped lang="less">
  #comment-component {
    width: 100%;
    height: 100px;

  }
</style>

<template>
  <div id="comment-component">
    <div class="write-wrapper">
      <write-comment-component/>
    </div>
  </div>
</template>

<script>
  import WriteCommentComponent from './WriteCommentComponent'

  export default {
    name: 'comment-component',
    components: {WriteCommentComponent}
  }
</script>
