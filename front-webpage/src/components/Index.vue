<style scoped lang="less">
  @import "../assets/my-style";

  #index {
    width: 100%;
    height: 100%;
    background: url("../assets/bg.gif") repeat;
  }

  .header {
    height: 25%;
    position: relative;

    .logo-wrapper {
      width: 30%;
      height: 100%;
      .flex(@h: flex-start);

      img {
        margin-left: 20px;
        height: 150px;
      }
    }
  }

  .container {
    position: relative;
    width: 100%;
    height: 75%;
    background-color: black;
  }
</style>

<template>
  <div id="index">
    <div class="header">
      <div class="logo-wrapper">
        <img src="../assets/logo.png" alt="早茶月光">
      </div>
    </div>
    <div class="container">

    </div>
  </div>
</template>

<script>
  export default {
    name: 'index'
  }
</script>
