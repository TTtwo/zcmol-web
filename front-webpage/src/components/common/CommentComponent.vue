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
        margin-top: 40px;

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
            color: #ff9ca9;
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
        background-color: #e4e4e4;
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
              background-color: #999;
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
              background-color: #bbb;
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
      <ul v-for="item, index in comments_data" class="ul-lv1">
        <li class="ul-lv1-li">
          <div class="avatar">
            <img :src="getAvatar(item.email, false)">
          </div>
          <div class="info-wrapper">
            <div class="info">
              <a :href="item.website" target="_blank">{{item.nickname}}</a>
              <span>Time: {{timeTransform(item.create_at)}}</span>
            </div>
            <aside class="aside">
              <div class="comment">
                <img @click="commentModal(item.id)" src="../../assets/comment.png">
              </div>
            </aside>
          </div>
          <div class="content">
            <p>-- {{item.content}}
            </p>
          </div>
          <sub-comment :comments="item.subComments" :id="id" @replyId="commentModal"></sub-comment>
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
            <input v-model="nickname" type="text" class="modal-input" placeholder="...">
          </div>
          <div class="modal-item">
            <div class="modal-title">邮箱</div>
            <input v-model="email" type="text" class="modal-input" placeholder="...">
          </div>
          <div class="modal-item">
            <div class="modal-title">网址</div>
            <input v-model="website" type="text" class="modal-input" placeholder="...">
          </div>
          <div class="modal-item">
            <div class="modal-title">内容</div>
            <textarea v-model="content" class="modal-textarea" placeholder="..."></textarea>
          </div>
          <div class="modal-item">
            <div class="modal-send-btn">
              <span @click="postComment">SEND</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="write-btn" @click="showModal">W</div>
  </div>
</template>
<script>
  import api from '../../api/api'
  import subComment from './subCommentComponent'
  import {timeTransform, getAvatar} from "../../util";

  export default {
    name: 'comment-component',
    components: {subComment},
    props: ["comments", "id"],
    data() {
      return {
        is_write: false,
        comments_data: [],
        nickname: '',
        content: '',
        website: '',
        email: '',
        reply_id: '',
      }
    },
    methods: {
      timeTransform: timeTransform,
      getAvatar: getAvatar,
      showModal() {
        this.is_write = !this.is_write
        if (!this.is_write) this.reply_id = ''
        return this.is_write
      },
      commentModal(reply_id) {
        this.reply_id = reply_id
        this.is_write = true
      },
      // 处理评论数据
      dataProcessing(data) {
        if (!data instanceof Array || data.length === 0) {
          this.comments_data = []
          return false
        }
        let new_data = []
        let temp = null
        for (var i = 0, len = data.length; i < len; i++) {
          for (var j = 0, lenj = data.length; j < lenj - 1 - i; j++) {
            if (data[j].id > data[j + 1].id) {
              temp = data[j]
              data[j] = data[j + 1]
              data[j + 1] = temp
            }
          }
        }
        for (var i = 0, len = data.length; i < len; i++) {
          data[i].subComments = []
          if (data[i].article_comment_id == null) {
            new_data.push(data[i])
          }
          else {
            this._findData(new_data, data[i])
          }
        }
        this.comments_data = new_data
      },
      _findData(data, target) {
        for (var i = 0, len = data.length; i < len; i++) {
          if (data[i].id === target.article_comment_id) {
            data[i].subComments.push(target)
            return true
          } else {
            this._findData(data[i].subComments, target)
          }
        }
      },

      async postComment() {
        if (!this.nickname || !this.content) {
          alert('数据不能为空!!')
          return false
        }
        const content = this.content
        this.content = ''
        localStorage.setItem('nickname', this.nickname)
        localStorage.setItem('website', this.website)
        localStorage.setItem('email', this.email)
        const result = await this.$$api(api.post_daily_comment,
          {
            body: {
              nickname: this.nickname,
              content: content,
              email: this.email ? this.email : '',
              website: this.website ? this.website : '',
              reply_id: this.reply_id ? this.reply_id : null
            },
            urlArgs: {
              id: this.id
            }
          })
        if (result.status !== 200) {
          alert('留言失败，请刷新页面重新尝试')
          return false
        }
        if (result.body.error === 2001) {
          alert('每次留言的时间间隔为30秒！')
          return false
        }
        this.$router.go(0)
      }

    },
    watch: {
      comments: function (co) {
        this.comments = co
        this.dataProcessing(this.comments)
      },
      id: function (id) {
        this.id = id
      }
    },
    mounted() {
      this.nickname = localStorage.getItem('nickname')
      this.website = localStorage.getItem('website')
      this.email = localStorage.getItem('email')
    }
  }
</script>
