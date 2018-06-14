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
          height: 400px;
          list-style: none;
          background-color: red;
          margin: 0 auto;
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
        <ul class="v-ul"></ul>
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
        is_paved: false
      }
    }
  }
</script>
