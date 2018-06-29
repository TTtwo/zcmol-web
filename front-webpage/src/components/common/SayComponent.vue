<style lang="less" scoped>
  #say {
    display: flex;
    flex-direction: row;
    overflow-y: scroll;
    div {
      width: 300px;
      height: auto;
      background-color: red;
      overflow-y: hidden;
      margin: 10px 10px;
    }
  }
</style>
<template>
  <div id="say">
    <div>adfasdfadfasdf</div>
    <div>aadfasdfadfasdfadfasdfadfasdfadfasdfadfasdfdfasdfadfasdf</div>
    <div>adfasdfadfasdf</div>
  </div>
</template>
<script>
  export default {
    name: 'say',
  }
</script>
