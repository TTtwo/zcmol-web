<style scoped lang="less">
  @import "../assets/my-style";

  #index {
    width: 100%;
    height: 100%;
    background: url("../assets/bg.gif") repeat;

    .header {
      height: 25%;
      position: relative;

      .logo-wrapper {
        width: 30%;
        height: 100%;
        .flex(@h: flex-start);

        .logo {
          width: 100%;
          height: 100%;
          max-height: 196px;
          max-width: 256px;
          background: url("../assets/logo.png") no-repeat center;
          background-size: contain;
        }
      }
    }

    .container {
      position: relative;
      width: 100%;
      height: 75%;
      background-color: black;
    }
  }
</style>

<template>
  <div id="index">
    <div class="header">
      <div class="logo-wrapper">
        <div class="logo"></div>
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
