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
        .msg-page {
          width: 20%;
          height: 28%;
          float: left;
          .flex(@h: space-around);
          .page-btn {
            width: 80px;
            height: 80px;
            border-radius: 80px;
            background-color: #7de87d;
            color: #3a3a3a;
            .flex;
            font-size: 60px;
            box-shadow: 0 0 5px #7de87d;
            &:hover {
              cursor: pointer;
              background-color: #3a3a3a;
              color: #7de87d;
            }
          }
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
                position: relative;
                float: left;
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
              position: relative;
              .ot-avatar {
                width: 60px;
                position: relative;
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
                .flex(@h: flex-end);
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
                min-height: 90px;
                min-width: 180px;
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
        .enter-name,
        .enter-content,
        .enter-email,
        .enter-website {
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

        .enter-email {
          width: 25%;
          top: -200%;
          left: -100%;
          background-color: #333;
          transition: left .6s ease-in-out;
          box-shadow: 0 -2px 5px #333;
          .icon {
            background: url("../../assets/me1.png") no-repeat center;
          }
        }
        .enter-website {
          width: 55%;
          top: -200%;
          left: 200%;
          background-color: #3a3a3a;
          box-shadow: 0 -2px 5px #3a3a3a;
          transition: left .6s ease-in-out;
          .icon {
            background: url("../../assets/messagebook1.png") no-repeat center;
          }
        }
        .enter-anim {
          left: 0;
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
          .enter-name, .enter-email {
            width: 30%;
          }
          .enter-content, .enter-website {
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
        <li v-for="item, index in guestbook_array" :key="index" class="msg-item">
          <div class="li-d1">
            <a :href="item.website" target="_blank">
              <div class="icon icon1"></div>
            </a>
            <div class="text">
              <p>{{item.nickname}}</p>
              <p>
                {{item.content}}
              </p>
            </div>
          </div>
          <div class="li-d2">
            <div class="icon icon2"></div>
            <div class="text">
              <p class="reply">
                {{item.my_reply}}
              </p>
            </div>
          </div>
        </li>
        <li class="msg-page">
          <div v-show="paging.has_prev" class="page-btn"
               @click="getData(paging.current_idx - 1)"><
          </div>
          <div v-show="paging.has_next" class="page-btn"
               @click="getData(paging.current_idx + 1)">>
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
          <li v-for="item, index in guestbook_array" :key="index" class="li-item">
            <!--<div class="li-time"><span>1分钟前</span></div>-->
            <div class="other">
              <div class="ot-avatar">
                <a :href="item.website" target="_blank"><img
                  src="http://storeweb.cn/upload/site/image/2018-04/193-4-XEOXQC.jpg"></a>
              </div>
              <div class="ot-context">
                <p class="ot-nickname">@{{item.nickname}}</p>
                <p class="ot-content">{{item.content}}</p>
              </div>
            </div>
            <div class="my-reply">
              <div class="my-avatar">
                <img src="../../assets/Icon.png" alt="">
              </div>
              <div class="my-context">
                <p class="my-nickname">Reply:</p>
                <p class="my-content">{{item.my_reply}}</p>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <div class="send-wrapper">
        <div class="enter-name">
          <div class="icon"></div>
          <input v-model="nickname" type="text" placeholder="输入昵称"
                 @focus="onFocus"
                 @blur="onBlur">
        </div>
        <div class="enter-content">
          <div class="icon"></div>
          <input v-model="content" type="text" placeholder="请输入内容  在回复之前都是[...]"
                 @focus="onFocus"
                 @blur="onBlur">
        </div>
        <div class="send-btn" @click="postData">SEND</div>
        <div class="enter-email" :class="{'enter-anim': show_other_input}">
          <div class="icon"></div>
          <input v-model="email" type="text" placeholder="输入邮箱"
                 @focus="onFocus"
                 @blur="onBlur">
        </div>
        <div class="enter-website" :class="{'enter-anim': show_other_input}">
          <div class="icon"></div>
          <input v-model="website" type="text" placeholder="输入网址"
                 @focus="onFocus"
                 @blur="onBlur">
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import api from '../../api/api'

  export default {
    name: 'guestbook',
    props: ['guestbooks'],
    data() {
      return {
        is_paved: true,
        show_other_input: false,
        screen_width: window.innerWidth,
        guestbook_array: this.guestbooks,
        paging: {
          current_idx: 1,
          has_next: true,
          has_prev: false,
          next_idx: null,
          prev_idx: null,
          total_pages: 2
        },
        per_page: 100,
        // post
        nickname: null,
        content: null,
        website: null,
        email: null
      }
    },
    methods: {
      onFocus() {
        this.show_other_input = true
      },
      onBlur() {
        this.show_other_input = false
      },
      reSize() {
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
      },
      async getData(page) {
        if (!page || page > this.paging.total_pages)
          return
        const result = await this.$$api(api.get_guestbook,
          {
            params: {
              page: page,
              per_page: this.per_page
            }
          })
        if (result.status !== 200) {
          this.$Message.error('访问失败~')
          return
        }
        this.guestbook_array = result.body.data.guestbook
        this.paging = result.body.data.paging
      },
      async postData() {
        if (!this.nickname || !this.content) {
          console.log('不能为空')
          return
        }
        await localStorage.setItem('nickname', this.nickname)
        await localStorage.setItem('website', this.website)
        await localStorage.setItem('email', this.email)
        console.log(this.email ? this.email : '')
        const result = await this.$$api(api.post_guestbook,
          {
            body: {
              nickname: this.nickname,
              content: this.content,
              email: this.email ? this.email : '',
              website: this.website ? this.website : ''
            }
          })
        this.content = null
        if (result.status === 200) {
          await this.getData(1)
        }
      }
    },
    mounted() {
      this.reSize()
      this.nickname = localStorage.getItem('nickname')
      this.website = localStorage.getItem('website')
      this.email = localStorage.getItem('email')
    }
  }
</script>
