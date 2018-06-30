<style lang="less" scoped>
  #say {
    overflow-y: scroll;
    .say-wrapper {
      -webkit-column-width: 400px;
      -moz-column-width: 400px;
      column-width: 400px;
      -webkit-column-gap: 5px;
      -moz-column-gap: 5px;
      column-gap: 5px;
      .say-item {
        padding: 20px;
        float: left;
        height: 100px;
        .say-content {
          height: 100px;
          background-color: red;
        }
      }
    }
  }
</style>
<template>
  <div id="say">
    <div class="say-wrapper">
      <div class="say-item">
        <div class="say-content">asdflasldfsadfs</div>
      </div>
      <div class="say-item">asldfjasldfjaskldfjVy</div>
      <div class="say-item">asldfjasldfjaskldfjVy</div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'say',
  }
</script>
