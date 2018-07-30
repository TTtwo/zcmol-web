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
      background-color: #323232;
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
        font-family: 'microsoft yahei', arial;
        .content-wrap {
          .title {
            padding: 60px 0 10px 0;
            font-size: 40px;
            color: #eee;
          }
          .info {
            font-size: 18px;
            color: #999;
            span:nth-child(2) {
              padding: 8px;
            }
          }
          .content {
            padding-top: 15px;
            padding-bottom: 40px;
            color: #bbb;
            font-size: 20px;
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
      box-shadow: 2px -2px 16px 4px #222;
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
      box-shadow: 2px 2px 16px 8px #222;
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
          <div class="title"><span>{{content.daily_content.title}}</span></div>
          <div class="info">
            <span>Time: {{timeTransform(content.create_at)}}</span>
            <span>丨</span>
            <span>Hits: 110</span>
          </div>
          <div class="content">
            {{content.daily_content.content}}
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
  import api from '../api/api'

  export default {
    name: 'daily_article',
    components: {CommentComponent},
    data() {
      return {
        is_show_comment: false,
        article_id: this.$route.params.id,
        content: {
          daily_content: {
            title: '',
            content: '',
          }
        },
        comments: []
      }
    },
    methods: {
      async getArticle() {
        const result = await this.$$api(api.get_daily, {
          urlArgs: {
            id: this.article_id
          }
        })
        if (result.status !== 200) {
          console.log('内容获取失败!')
          return
        }
        if (!result.body.article) {
          console.log('内容不存在!')
          return
        }
        this.content = result.body.article
      },
      async getComment() {
        const result = await this.$$api(api.get_daily_comment, {
          urlArgs: {
            id: this.article_id
          }
        })
        if (result.status !== 200) {
          console.log('数据获取失败！')
          return
        }
        const data = result.body.comments
        this.dataHandle(data)
      },
      dataHandle(data) {
        if (!data) return
        for (var i = 0; i < data.length; i++) {
          if (data[i].article_comment_id == null) {
            let d = data[i]
            d.subComments = []
            this.comments.push(d)
          } else {

          }
        }
      },
      timeTransform(time) {
        const date = new Date(time * 1000)
        const yms = date.toLocaleDateString().replace(new RegExp('/', 'g'), '.')
        const hms = date.toLocaleTimeString()
        return yms + hms
      },
    },
    mounted() {
      if (!this.article_id) {
        console.log('123123123')
        this.$router.push('index')
        return
      }
      this.getArticle()
      this.getComment()
    }
  }
</script>
