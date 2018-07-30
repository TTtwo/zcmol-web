<style scoped lang="less">
  @import "../../assets/my-style";

  #comment-component {
    width: 100%;
    height: 100%;
    overflow-x: hidden;
    overflow-y: scroll;
    .content-wrapper {
      margin: 20px 60px;

      .ul-lv1 {
        list-style: none;
        overflow-x: scroll;
        .ul-lv1-li {
          width: 100%;
          text-align: left;
          position: relative;
          padding: 1px;
          margin-top: 2px;
          &::after {
            content: '';
            display: block;
            visibility: hidden;
            height: 0;
            clear: both;
          }
          .avatar {
            width: 70px;
            height: 70px;
            overflow: hidden;
            box-shadow: 0 0 5px @comment_bg;
            transition: border-radius .5s ease-in-out;
            float: left;
            img {
              width: 70px;
              height: 70px;
            }
          }
          .info-wrapper {
            float: left;
            margin-left: 10px;
            height: 80px;
            color: @comment_bg;
            font-size: 20px;
            font-family: beleren;
            .info {
              height: 80px;
              position: relative;
              float: left;
              span {
                display: block;
                color: #999;
                height: 50%;
                .flex(@h: flex-start);
              }
              a {
                font-size: 24px;
                display: block;
                height: 50%;
                color: #bababa;
                .flex(@h: flex-start;@v: flex-start);
                &:hover {
                  color: @green;
                }
              }
            }
            .aside {
              height: 80px;
              width: 80px;
              position: relative;
              float: left;
              display: none;

              .comment {
                height: 50px;
                width: 50px;
                background-color: @barColor;
                -webkit-border-radius: 50px;
                -moz-border-radius: 50px;
                border-radius: 50px;
                .flex;
                img {
                  width: 25px;
                  height: 25px;
                  &:hover {
                    opacity: .6;
                    cursor: pointer;
                  }
                }
              }
            }
            &:hover .aside {
              .flex;
            }
          }
          .content {
            position: relative;
            margin: 80px 0 20px 0;
            text-indent: 2em;
            padding-left: 80px;
            font-size: 24px;
            line-height: 36px;
            color: @comment_bg;
          }
        }
      }
      .ul-lv2 {
        padding-left: 80px;
      }

    }
    .write-btn {
      .circle-btn;
      position: absolute;
      right: 12px;
      top: 90px;
    }
    .modal {
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      opacity: 0;
      visibility: hidden;
      transition: opacity .2s ease-in-out, visibility .2s ease-in-out;
      .flex;
      .modal-mask {
        width: 100%;
        height: 100%;
        background-color: #333333;
        opacity: .5;
      }
      .modal-wrapper {
        width: 680px;
        min-height: 200px;
        background-color: white;
        position: absolute;
        top: 40px;
        border-radius: 10px;
        -webkit-box-shadow: 0 0 5px #222;
        -moz-box-shadow: 0 0 5px #222;
        box-shadow: 0 0 5px #222;
        .modal-header {
          height: 40px;
          width: 100%;
          -webkit-box-sizing: border-box;
          -moz-box-sizing: border-box;
          box-sizing: border-box;
          border-bottom: 1px solid #777;
          color: black;
          font-weight: bolder;
          font-size: 18px;
          .flex;
        }
        .modal-content {
          padding: 5px 10px;
          .modal-item {
            position: relative;
            margin-bottom: 10px;
            .modal-title {
              height: 44px;
              font-size: 24px;
              font-weight: bolder;
              color: #222;
              background-color: #cce8cf;
              .flex(@h: flex-start);
              -webkit-box-sizing: border-box;
              -moz-box-sizing: border-box;
              box-sizing: border-box;
              padding-left: 10px;
              border-radius: 5px;
            }
            .modal-input, .modal-textarea {
              width: 100%;
              border: none;
              outline: none;
              -webkit-box-sizing: border-box;
              -moz-box-sizing: border-box;
              box-sizing: border-box;
              padding-left: 10px;
              font-size: 24px;
              background-color: #e6e7ee;
            }
            .modal-input {
              height: 60px;
            }
            .modal-textarea {
              height: 80px;
              resize: vertical;
              line-height: 36px;
              padding: 10px;
            }
            .modal-send-btn {
              width: 100%;
              .flex(@h: flex-end);
              span {
                width: 100px;
                height: 50px;
                border-radius: 5px;
                color: #d2d2d2;
                background-color: #1c2a3a;
                font-family: beleren;
                font-size: 24px;
                .flex;
                &:hover {
                  color: #1c2a3a;
                  background-color: #d2d2d2;
                  cursor: pointer;
                }
              }
            }
          }
        }
      }
    }
    .modal-anim {
      visibility: unset;
      opacity: 1;
    }
  }

</style>

<template>
  <div id="comment-component">
    <div class="content-wrapper">
      <ul v-for="item, index in array" class="ul-lv1">
        <li class="ul-lv1-li">
          <div class="avatar">
            <img src="../../assets/logo.png">
          </div>
          <div class="info-wrapper">
            <div class="info">
              <a href="http://zcmol.cn" target="_blank">{{item.nickname}}</a>
              <span>Time: 2016:03:06 23:54:46</span>
            </div>
            <aside class="aside">
              <div class="comment">
                <img src="../../assets/comment.png">
              </div>
            </aside>
          </div>
          <div class="content">
            <p>-- {{item.content}}
            </p>
          </div>
          <sub-comment :comments="item.subComments"></sub-comment>
        </li>
      </ul>
    </div>
    <div class="modal" :class="{'modal-anim': is_write}">
      <div class="modal-mask" @click="is_write = false"></div>
      <div class="modal-wrapper">
        <div class="modal-header">嘿, 写点什么吧</div>
        <div class="modal-content">
          <div class="modal-item">
            <div class="modal-title">昵称</div>
            <input type="text" class="modal-input" placeholder="...">
          </div>
          <div class="modal-item">
            <div class="modal-title">邮箱</div>
            <input type="text" class="modal-input" placeholder="...">
          </div>
          <div class="modal-item">
            <div class="modal-title">网址</div>
            <input type="text" class="modal-input" placeholder="...">
          </div>
          <div class="modal-item">
            <div class="modal-title">内容</div>
            <textarea class="modal-textarea" placeholder="..."></textarea>
          </div>
          <div class="modal-item">
            <div class="modal-send-btn">
              <span>SEND</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="write-btn" @click="is_write = !is_write">W</div>
  </div>
</template>

<script>
  import api from '../../api/api'
  import subComment from './subCommentComponent'

  export default {
    name: 'comment-component',
    components: {subComment},
    data() {
      return {
        is_write: false,
        array: [
          {
            nickname: '123',
            content: '1231231231',
            subComments: [
              {
                nickname: '455',
                content: '4545454',
                subComments: []
              }
            ]
          },
          {
            nickname: '你好我',
            content: '<div>哈哈</div>',
            subComments: [
              {
                nickname: '打发了斯蒂芬',
                content: '45454d阿瑟的发放4',
                subComments: []
              }
            ]
          }
        ]
      }
    },
  }
</script>
