<style lang="less" scoped>
  @import "../../assets/my-style";

  #guestbook {
    .container {
      width: 100%;
      height: 100%;
      overflow-y: hidden;
      .paved, .vertical {
        width: 100%;
        height: 100%;
        overflow-y: scroll;
        padding-bottom: 88px;
      }
      .paved {
        list-style: none;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
        .msg-item {
          width: 20%;
          height: 28%;
          float: left;
          border: 1px solid #222;
          -webkit-box-sizing: border-box;
          -moz-box-sizing: border-box;
          box-sizing: border-box;
          position: relative;
          overflow: hidden;
          .li-d1, .li-d2 {
            width: 100%;
            height: 50%;
            float: left;
          }
          .li-d1 {
            background-color: @green;
            transition: height .2s ease-in-out;
          }
          .li-d2 {
            background-color: #3a3a3a;
            position: absolute;
            bottom: 0;
            transition: bottom .2s ease-in-out, height .2s ease-in-out;
            -webkit-box-shadow: 0 0 6px #3a3a3a;
            -moz-box-shadow: 0 0 6px #3a3a3a;
            box-shadow: 0 0 6px #3a3a3a;
            &::before {
              content: '';
              border-top: 1px solid #3a3a3a;
              border-left: 1px solid #3a3a3a;
              -webkit-box-shadow: 0 0 6px #3a3a3a;
              -moz-box-shadow: 0 0 6px #3a3a3a;
              box-shadow: 0 0 6px #3a3a3a;
              position: absolute;
              -webkit-border-radius: 5px;
              -moz-border-radius: 5px;
              border-radius: 5px;
              top: -8px;
              left: 32px;
              width: 20px;
              height: 20px;
              transform: rotate(45deg);
              background-color: #3a3a3a;
            }
            &:hover {
              height: 70%;
            }
          }
          .li-d1:hover + .li-d2 {
            bottom: -20%;
          }
          .li-d1:hover {
            height: 70%;
          }
          &:hover {
            cursor: default;
          }
        }
        .msg-item:first-child {
          width: 40%;
        }
        .icon {
          float: left;
          -webkit-box-sizing: border-box;
          -moz-box-sizing: border-box;
          box-sizing: border-box;
          width: 80px;
          height: 80px;
          margin: 4px 0 0 4px;
          background-size: cover;

        }
        .icon1 {
          background: url("../../assets/me.png") no-repeat center;
          &:hover {
            cursor: pointer;
          }
        }
        .icon2 {
          background: url("../../assets/messagebook1.png") no-repeat center;
        }
        .text {
          -webkit-box-sizing: border-box;
          -moz-box-sizing: border-box;
          box-sizing: border-box;
          margin-left: 100px;
          position: absolute;
          padding: 10px 20px 10px 0px;
          p {
            text-align: left;
          }
          .reply {
            color: #b6b6b6;
            padding-top: 10px;
          }
        }
      }
      .vertical {
        text-align: center;
        .v-ul {
          width: 1200px;
          list-style: none;
          margin: 0 auto;
          padding-bottom: 88px;
          .li-tip {
            padding: 10px 0;
            height: 80px;
            width: 100%;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            .flex;
            .tip {
              width: 50%;
              max-width: 400px;
              height: 100%;
              border-radius: 90px;
              background-color: #3a3a3a;
              .tip-avatar {
                height: 60px;
                width: 60px;
                border-radius: 60px;
                position: absolute;
                background: url("../../assets/Icon1.png") no-repeat center;
                background-size: cover;
              }
              p {
                height: 100%;
                .flex;
                font-size: 24px;
                color: @green;
              }
            }
          }
          .li-item {
            width: 100%;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            padding: 10px 20px;
            position: relative;
            .li-time {
              padding: 10px;
              .flex;
              span {
                width: 160px;
                border-radius: 20px;
                background-color: @green;
                color: #222;
                font-size: 18px;
                padding: 4px 0;
                .flex;
              }
            }
            .other {
              .ot-avatar {
                width: 60px;
                position: relative;
                float: left;
                img {
                  width: 60px;
                  height: 60px;
                  border-radius: 60px;
                  box-shadow: 0 0 10px @green;
                }
                &:hover {
                  cursor: pointer;
                }
              }
              .ot-context {
                position: relative;
                float: left;
                background-color: @green;
                p {
                  padding: 0 20px;
                  text-align: left;
                  font-size: 24px;
                  color: #222;
                }
                .ot-nickname {
                  padding-top: 10px;
                  font-weight: bolder;
                }
                .ot-content {
                  padding-top: 5px;
                  padding-bottom: 10px;
                }
              }
            }
            .my-reply {
              padding-top: 10px;
              .my-avatar {
                position: relative;
                float: right;
                img {
                  width: 60px;
                  height: 60px;
                  border-radius: 60px;
                  box-shadow: 0 0 10px @comment_bg;
                }
              }
              .my-context {
                position: relative;
                float: right;
                background-color: #3a3a3a;
                p {
                  padding: 0 20px;
                  font-size: 24px;
                  color: #999;
                  text-align: left;
                }
                .my-nickname {
                  padding-top: 10px;
                  font-weight: bolder;
                }
                .my-content {
                  padding-top: 5px;
                  padding-bottom: 10px;
                }
              }
            }
            .my-reply, .other {
              .ot-context, .my-context {
                margin-left: 85px;
                margin-right: 85px;
                margin-top: -60px;
                border-radius: 10px;
                -webkit-box-sizing: border-box;
                -moz-box-sizing: border-box;
                box-sizing: border-box;
              }
              &::after {
                content: '';
                visibility: hidden;
                height: 0;
                display: block;
                clear: both;
              }
            }
          }
        }
        @media (max-width: 960px) {
          .v-ul {
            width: 100%;
          }
        }
      }
      .send-wrapper {
        height: 88px;
        width: 100%;
        position: absolute;
        bottom: 0;
        background-color: #333;
        -webkit-box-shadow: 0 0 20px 4px #222;
        -moz-box-shadow: 0 0 20px 4px #222;
        box-shadow: 0 0 20px 4px #222;
        .enter-name, .enter-content, .enter-email, .enter-website {
          position: relative;
          float: left;
          height: 100%;
          .flex(@h: flex-start);
          .icon {
            width: 60px;
            height: 60px;
            position: relative;
            margin-left: 14px;
            background-size: cover;
          }
          input {
            display: block;
            position: absolute;
            height: 100%;
            width: calc(100% - 100px);
            left: 100px;
            border: none;
            outline: none;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            padding: 0 10px;
            background-color: transparent;
            font-size: 24px;
            color: #888;
          }
        }
        .enter-name {
          width: 25%;
          background-color: #3a3a3a;
          .icon {
            background: url("../../assets/me1.png") no-repeat center;
          }
        }
        .enter-content {
          width: 55%;
          .icon {
            background: url("../../assets/messagebook1.png") no-repeat center;
          }
        }
        .send-btn {
          position: relative;
          float: left;
          width: 20%;
          height: 100%;
          background-color: @green;
          font-size: 50px;
          font-family: 'impact', arial;
          overflow: hidden;
          .flex;
          &:hover {
            cursor: pointer;
            background-color: #97ef97;
          }
        }
      }
      @media (max-width: 960px) {
        .send-wrapper {
          .enter-name {
            width: 30%;
          }
          .enter-content {
            width: 60%;
          }
          .send-btn {
            width: 10%;
            font-size: 38px;
          }
        }
      }
    }
  }
</style>
<template>
  <div id="guestbook">
    <div class="container">
      <ul v-if="is_paved" class="paved">
        <li class="msg-item">
          <div class="li-d1">
            <a href="http://zcmol.cn" target="_blank">
              <div class="icon icon1"></div>
            </a>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
        <li class="msg-item">
          <div class="li-d1">
            <div class="icon icon1"></div>
            <div class="text">
              <p>奈何</p>
              <p>
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                我是爱着你的， 哈哈阿斯顿发生了的纠纷阿斯利康大姐夫 加收代理费加速度快放假哈克斯地方哈士大夫阿斯蒂芬
              </p>
            </div>
          </div>
        </li>
      </ul>
      <div v-else class="vertical">
        <ul class="v-ul">
          <li class="li-tip">
            <div class="tip">
              <div class="tip-avatar"></div>
              <p>回复之前都是[...]</p>
            </div>
          </li>
          <li class="li-item">
            <div class="li-time"><span>1分钟前</span></div>
            <div class="other">
              <div class="ot-avatar">
                <a href="http://zcmol.cn" target="_blank"><img
                  src="http://storeweb.cn/upload/site/image/2018-04/193-4-XEOXQC.jpg"></a>
              </div>
              <div class="ot-context">
                <p class="ot-nickname">@我是你好</p>
                <p class="ot-content">楼上的房间氨基酸老地方阿斯兰的积分阿斯兰的风景阿斯兰的咖啡机阿斯兰地方加收代理费加点水j</p>
              </div>
            </div>
            <div class="my-reply">
              <div class="my-avatar">
                <img src="../../assets/Icon.png" alt="">
              </div>
              <div class="my-context">
                <p class="my-nickname">Reply:</p>
                <p class="my-content">打发斯楼上的房间氨基酸老地方阿斯兰的积分阿斯兰的风景阿斯兰的咖啡机阿斯兰地方加收代理费加点水j蒂芬</p>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <div class="send-wrapper">
        <div class="enter-name">
          <div class="icon"></div>
          <input type="text" placeholder="输入昵称">
        </div>
        <div class="enter-content">
          <div class="icon"></div>
          <input type="text" placeholder="请输入内容  在回复之前都是[...]">
        </div>
        <div class="send-btn">SEND</div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'guestbook',
    data() {
      return {
        is_paved: true,
        screen_width: window.innerWidth
      }
    },
    mounted() {
      window.innerWidth < 1024
        ? this.is_paved = false
        : this.is_paved = true

      let func
      const self = this
      window.onresize = function () {
        if (func)
          clearTimeout(func)
        func = setTimeout(() => {
          window.innerWidth < 1024
            ? self.is_paved = false
            : self.is_paved = true
        }, 200)
      }
    }
  }
</script>
