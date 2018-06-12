<style scoped lang="less">
  @import "../assets/my-style";

  #motto {
    width: 100%;
    height: 100%;
    overflow: hidden;
    .bg {
      width: 100%;
      height: 100%;
      background: url("../assets/motto-bg.jpg") center no-repeat;
      background-size: cover;
      filter: grayscale(100%);
      opacity: .9;
    }
    .bg-wrapper {
      height: 100%;
      top: -100%;
      position: relative;
      text-align: center;
      .flex;
      .lo {
        position: relative;
        padding: 0 40px;
        color: white;
        > span {
          font-family: motto;
          display: block;
          font-size: 160px;
          text-align: center;
          line-height: 140px;
          letter-spacing: -10px;
          text-shadow: 0 0 20px #333333;
        }
        .say {
          width: 100%;
          position: relative;
          top: 28px;
          font-size: 28px;
          font-family: motto;
          color: @comment_bg;
        }
        .read {
          width: 100%;
          height: 80px;
          position: relative;
          margin-top: 120px;
          .flex;
          span {
            @size: 80px;
            width: @size;
            height: @size;
            color: #000;
            font-size: 64px;
            font-family: motto;
            background-color: @green;
            display: block;
            -webkit-border-radius: @size;
            -moz-border-radius: @size;
            border-radius: @size;
            .flex;
            &:hover {
              cursor: pointer;
              border: 1px solid @green;
              background-color: initial;
              -webkit-box-sizing: border-box;
              -moz-box-sizing: border-box;
              box-sizing: border-box;
            }
          }
        }
      }
      .logo {
        position: absolute;
        right: 20px;
        top:  20px;
        @size: 80px;
        height: @size;
        width: @size;
        .flex;
        -webkit-border-radius: @size;
        -moz-border-radius: @size;
        border-radius: @size;
        font-family: motto;
        background: url("../assets/logo.png") no-repeat center;
        background-size: contain;
        border: 1px solid @green;
      }
    }
  }
</style>

<template>
  <div id="motto">
    <div class="bg"></div>
    <div class="bg-wrapper">
      <div class="lo">
        <span>心灵</span>
        <span>鸡汤</span>
        <div class="say">
          <span>
            琐碎事情不多，日子过得简单。<br>
            听听歌，看看电影，打打球。我养了植物，时不时的会出去走走，太阳跟雨都喜欢
          </span>
        </div>
        <div class="read"><span>读</span></div>
      </div>
      <div class="logo"></div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'motto'
  }
</script>
