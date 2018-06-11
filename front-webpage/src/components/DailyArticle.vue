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
      overflow: hidden;

      .comment-wrapper {
        z-index: 5;
        width: 100%;
        height: 100%;
        position: absolute;
        overflow-y: scroll;
        top: -100%;
        /*background: url("../assets/bg.gif") repeat;*/
        background-color: #414141;
        -webkit-transition: top .7s;
        -moz-transition: top .7s;
        -ms-transition: top .7s;
        -o-transition: top .7s;
        transition: top .7s;
        transition-timing-function: ease-in-out;
      }
      .comment-wrapper-animation {
        top: 0;
      }
      .content-wrapper {
        z-index: 4;
        position: relative;
        width: 100%;
        height: 100%;
        overflow-y: scroll;
        .content-wrap {
          .title {
            padding: 40px 0 10px 0;
            font-size: 40px;
            color: @comment_bg;
            font-family: beleren;
          }
          .info {
            font-size: 24px;
            color: #777;
            font-family: beleren;
            span {
              display: block;
            }
          }
          .content {
            padding-top: 15px;
            padding-bottom: 40px;
            color: @comment_bg;
            font-size: 24px;
            line-height: 48px;
          }
        }
      }
    }

    .comment-btn {
      .circle-btn;
      position: absolute;
      top: 120px;
      right: 20px;
      z-index: 2;
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
        background-size: contain;
        &:hover {
          cursor: pointer;
        }
      }
    }
    .footer {
      bottom: 0;
      height: 80px;
      box-shadow: 2px 2px 16px #222;
      .btn:first-child {
        background-color: #404040;
      }
      .btn {
        width: 50%;
        height: 100%;
        float: left;
        font-family: beleren;
        font-size: 45px;
        color: @comment_bg;
        box-sizing: border-box;
        .flex;

        &:hover {
          background-color: @green;
          color: @barColor;
          cursor: pointer;
        }
      }

    }
  }
</style>

<template>
  <div id="daily_article">
    <div class="header">
      <a href="http://zcmol.cn">
        <div class="logo"></div>
      </a>
    </div>
    <div class="daily-container">
      <div class="comment-wrapper" :class="{'comment-wrapper-animation': is_show_comment}">
        <comment-component></comment-component>
      </div>
      <div class="content-wrapper">
        <div class="content-wrap">
          <div class="title"><span>你好</span></div>
          <div class="info">
            <span>Tag: log++</span>
            <span>Time: 2016.10.21 10:50:25</span>
          </div>
          <div class="content">
            <iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86
                    src="//music.163.com/outchain/player?type=2&id=361493&auto=0&height=66"></iframe>
            <br>
            我一直认为，你就是我的唯一<br>
            我一直认为，你就是我的唯一<br>
            我一直认为，你就是我的唯一<br>
            我一直认为，你就是我的唯一<br>
            我一直认为，你就是我的唯一<br>
            我一直认为，你就是我的唯一<br>
            我一直认为，你就是我的唯一<br>
            我一直认为，你就是我的唯一<br>
            我一直认为，你就是我的唯一<br>
            我一直认为，你就是我的唯一<br>
            我一直认为，你就是我的唯一<br>
            我一直认为，你就是我的唯一<br>
          </div>
        </div>
      </div>
    </div>
    <div class="comment-btn" @click="is_show_comment = !is_show_comment">C</div>
    <div class="footer">
      <div class="btn">Prev</div>
      <div class="btn">Next</div>
    </div>
  </div>
</template>

<script>
  import CommentComponent from './common/CommentComponent';

  export default {
    name: 'daily_article',
    components: {CommentComponent},
    data() {
      return {
        is_show_comment: false,
      }
    },
    methods: {}
  }
</script>
