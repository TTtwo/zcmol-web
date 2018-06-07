<style scoped lang="less">
  @import "../assets/my-style";

  #daily_article {
    width: 100%;
    height: 100%;

    .daily-container {
      z-index: 1;
      position: absolute;
      top: 100px;
      bottom: 80px;
      width: 100%;
      background: url("../assets/bg.gif");
      overflow-y: scroll;

      .content-wrapper {
        position: relative;
        margin: 40px;
      }

      .comment-btn {
        @c-size: 70px;
        width: @c-size;
        height: @c-size;
        position: absolute;
        font-size: @c-size - 10px;
        color: @barColor;
        font-family: beleren;
        -webkit-border-radius: @c-size;
        -moz-border-radius: @c-size;
        border-radius: @c-size;
        background-color: @green;
        .flex;
      }
    }

    .header, .footer {
      z-index: 2;
      width: 100%;
      background-color: @barColor;
      position: fixed;
    }
    .header {
      top: 0;
      height: 100px;
      box-shadow: 2px -2px 16px #222;
      border-bottom: 5px solid #3a3a3a;
      .flex;

      .logo {
        height: 95px;
        width: 95px;
        background: url("../assets/logo.png") no-repeat center;
        background-size: cover;
        &:hover {
          cursor: pointer;
        }
      }
    }
    .footer {
      bottom: 0;
      height: 80px;
      box-shadow: 2px 2px 16px #222;
      .btn {
        width: 50%;
        height: 100%;
        float: left;
        font-family: beleren;
        font-size: 45px;
        color: @green;
        box-sizing: border-box;
        .flex;

        &:hover {
          background-color: @green;
          color: @barColor;
          cursor: pointer;
        }
      }
      .btn:first-child {
        border-right: 1px solid #868686;
      }
      .btn:nth-child(2) {
        border-left: 1px solid #868686;
      }
    }
  }
</style>

<template>
  <div id="daily_article">
    <div class="header">
      <div class="logo"></div>
    </div>
    <div class="daily-container">
      <div class="content-wrapper">
      </div>
      <div class="comment-btn">C</div>
    </div>
    <div class="footer">
      <div class="btn">Prev</div>
      <div class="btn">Next</div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'daily_article'
  }
</script>
