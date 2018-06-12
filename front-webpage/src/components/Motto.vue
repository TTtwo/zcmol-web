<style scoped lang="less">
  @import "../assets/my-style";

  #motto {
    width: 100%;
    height: 100%;
    overflow: hidden;
    .bg-wrapper {
      height: 100%;
      width: 100%;
      top: -100%;
      position: relative;
      text-align: center;
      overflow: hidden;
      .bg {
        width: 100%;
        height: 100%;
        background: url("../assets/motto-bg.jpg") center no-repeat;
        background-size: cover;
        filter: grayscale(100%);
        opacity: .9;
      }
      .lo-wrapper {
        height: 100%;
        position: relative;
        top: -100%;
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
      }
    }
    .content-wrapper {
      width: 100%;
      height: 100%;
      position: relative;
      background-color: @comment_bg;
      .content-header {
        height: 145px;
        width: 100%;
        position: fixed;
        .flex;
        span {
          font-size: 100px;
          font-family: motto;
          text-shadow: 0 0 16px #777;
        }

      }
      .content {
        position: absolute;
        top: 145px;
        bottom: 0;
        right: 0;
        left: 0;
        overflow-y: scroll;
        .motto {
          width: 600px;
          padding: 20px;
          margin: 0 auto;
          text-align: center;
          color: #222;
          span {
            display: block;
            padding: 10px 20px;
            font-size: 24px;
          }
          .hx {
            .flex;
            div {
              width: 60px;
              border-radius: 5px;
              height: 2px;
              background-color: #777;
            }
          }
          .esll {
            padding-top: 40px;
            color: #777;
          }
          .words {
            line-height: 40px;
          }
        }
      }
    }
    .logo-wrapper {
      position: absolute;
      right: 0;
      top: 0;
      border-top: 150px solid @barColor;
      border-left: 150px solid transparent;
      .logo {
        left: -80px;
        top: -150px;
        position: absolute;
        width: 80px;
        height: 80px;
        background: url("../assets/logo.png") no-repeat center;
        background-size: contain;
        &:hover {
          cursor: pointer;
        }
      }
    }
  }
</style>

<template>
  <div id="motto">
    <div class="content-wrapper">
      <div class="content-header">
        <span>心灵鸡汤</span>
      </div>
      <div class="content">
        <div class="motto">
          <span>2016.12.06</span>
          <span class="words">没有了过去，就连未来也看不清打法是否阿斯顿发挥卡迪夫
          阿斯顿发生卡萨丁方括号阿斯蒂芬狂欢节
          阿斯顿发瘦客户机</span>
          <span class="hx"><div></div></span>
          <span>冯业佳  《天下》</span>
          <span class="esll">●●●</span>
        </div>
      </div>
    </div>
    <div v-show="false" class="bg-wrapper">
      <div class="bg"></div>
      <div class="lo-wrapper">
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
      </div>
    </div>
    <div class="logo-wrapper">
      <a href="http://zcmol.cn">
        <div class="logo"></div>
      </a>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'motto',
    data() {
      return {}
    }
  }
</script>
