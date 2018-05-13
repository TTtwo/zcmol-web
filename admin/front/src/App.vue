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

  .table {
    @marginLeft: 20px;
    .content-ul-title {
      width: 100%;
      height: 70px;
      position: relative;
      font-size: 22px;
      background-color: @green;
      color: @white;
      div {
        height: 100%;
        margin-left: @marginLeft;
        position: relative;
        float: left;
        display: flex;
        align-items: center;
        justify-self: flex-start;
      }
    }
    .content-ul {
      width: 100%;
      li {
        width: 100%;
        height: 70px;
        position: relative;
        font-size: 22px;
        &:hover {
          cursor: pointer;
          background-color: @green-white;
        }
      }
      li > div {
        position: relative;
        float: left;
        height: 100%;
        line-height: 70px;
        white-space: nowrap;
        margin-left: @marginLeft;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        span {
          display: block;
          text-overflow: ellipsis;
          overflow: hidden;
          word-break: keep-all;
          height: 100%;
          width: 100%;
        }
      }
    }
  }

  .modal {
    .modal-wrap {
      margin-bottom: 15px;

      .modal-title {
        width: 100%;
        height: 60px;
        font-size: 24px;
        font-weight: bold;
        position: relative;
        background-color: @green-white;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        span {
          height: 100%;
          position: relative;
          margin-left: 10px;
        }
      }
      .model-content {
        width: 100%;
        position: relative;
        font-size: 24px;
        background-color: @white-gray;
        line-height: 44px;
        span {
          width: 100%;
          position: relative;
          margin-left: 10px;
        }
      }
    }
  }

</style>
