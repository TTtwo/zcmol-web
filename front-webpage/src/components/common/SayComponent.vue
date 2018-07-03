<style lang="less" scoped>
  #say {
    overflow-y: scroll;

    .say-wrapper {
      display: grid;
      grid-gap: 100px;
      width: 100%;
      height: auto;

      .say-content {
        height: 100px;
        width: 200px;
        background-color: red;
      }

    }
  }
</style>
<template>
  <div id="say"></div>
</template>
<script>
  export default {
    name: 'say',
  }
</script>
