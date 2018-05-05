<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>

<style lang="less">
  @import "./assets/my-style";

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    width: 100%;
    height: 100%;
  }

  .full {
    width: 100%;
    height: 100%;
  }

  .wrap {
    width: 100%;
    height: 100%;
    overflow-y: scroll;
  }

  @media (max-width: 1024px) {
    .wrap {
      overflow: scroll;
    }
  }
</style>
