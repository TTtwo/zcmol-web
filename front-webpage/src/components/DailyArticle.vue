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
        background: url("../../static/logo.png") no-repeat center;
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
    .i-loader {
      z-index: 10;
      position: absolute;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      .flex;
      background-color: #222;
      > div {
        position: relative;
        .flex;
        > img {
          width: 100px;
          position: absolute;
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
        <comment-component :comments="comments" :id="$route.params.id"></comment-component>
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
      <div class="btn" @click="otherPage(content.prev)">Prev</div>
      <div class="btn" @click="otherPage(content.next)">Next</div>
    </div>
    <div class="i-loader" v-if="loading">
      <div>
        <img src="../../static/logo.png">
        <pacman-loader :color="'#7de87d'" :size="'100px'"></pacman-loader>
      </div>
    </div>
  </div>
</template>
<script>
  import CommentComponent from './common/CommentComponent';
  import PacmanLoader from "vue-spinner/src/ClipLoader";
  import api from '../api/api'
  import {timeTransform} from '../util'

  export default {
    name: 'daily_article',
    components: {CommentComponent, PacmanLoader},
    data() {
      return {
        loading: true,
        is_show_comment: false,
        article_id: this.$route.params.id,
        content: {
          daily_content: {}
        },
        comments: [],
        title: ''
      }
    },
    methods: {
      timeTransform: timeTransform,
      async getArticle() {
        this.loading = true
        this.article_id = this.$route.params.id
        const result = await this.$$api(api.get_daily, {
          urlArgs: {
            id: this.article_id
          }
        })
        if (result.status !== 200) {
          alert('内容获取失败!')
          return false
        }
        if (!result.body.article) {
          alert('内容不存在!')
          this.$router.push('index')
        }
        this.content = result.body.article
        document.title = this.content.daily_content.title
        await this.getComment()
        this.loading = false
      },
      async getComment() {
        const result = await
          this.$$api(api.get_daily_comment, {
            urlArgs: {
              id: this.article_id
            }
          })
        if (result.status !== 200) {
          alert('数据获取失败！')
          return
        }
        this.comments = result.body.comments
        console.log(this.comments)
      },
      otherPage(article_id) {
        if (article_id == null)
          return null
        console.log(article_id)
        this.$router.push('/' + article_id + '/daily_article')
      }
    },
    watch: {
      '$route': 'getArticle'
    },
    computed: {
      getTitle() {
        return this.title
      }
    },
    mounted() {
      if (!this.article_id) {
        this.$router.push('index')
        return false
      }
      this.getArticle()
    }
  }
</script>
