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
      transition: top .6s ease-in-out;
      .bg {
        width: 100%;
        height: 100%;
        background: url("../assets/motto-bg.jpg") center no-repeat;
        background-size: cover;
        filter: grayscale(50%);
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
                color: @comment_bg;
                border: 1px solid @comment_bg;
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
    .bg-wrapper-anim {
      top: -200%;
    }
    .content-wrapper {
      width: 100%;
      height: 100%;
      position: relative;
      background-color: @comment_bg;
      .content-header {
        top: -145px;
        height: 145px;
        width: 100%;
        position: fixed;
        .flex;
        transition: top .6s ease-in-out .6s;
        span {
          font-size: 100px;
          font-family: motto;
          text-shadow: 0 0 16px #777;
        }

      }
      .content-header-anim {
        top: 0;
      }
      .content-bg {
        position: relative;
        height: 100%;
        width: 100%;
        .flex;
        font-size: 400px;
        font-family: motto;
        opacity: .1;
      }
      .lizi {
        position: absolute;
        top: 145px;
        bottom: 0;
        left: 0;
        right: 0;
        opacity: .6;
      }
      @media (max-width: 880px) {
        .content-bg {
          font-size: 200px;
        }
      }
      @media (max-width: 1024px) {
        .lizi {
          display: none;
        }
      }
      .content {
        position: absolute;
        top: 600px;
        bottom: 0;
        right: 0;
        left: 0;
        overflow-y: scroll;
        transition: top 1.2s ease-in-out;

        .motto {
          width: 600px;
          padding: 20px;
          margin: 0 auto;
          text-align: center;
          color: #222;
          font-family: "WenQuanYi Micro Hei,
                        sans-serif";
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
      .content-anim {
        top: 145px;
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
        background: url("../../static/logo.png") no-repeat center;
        background-size: contain;
        &:hover {
          cursor: pointer;
        }
      }
    }
    .i-loader {
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
  <div id="motto">
    <div class="content-wrapper">
      <div class="content-header" :class="{'content-header-anim': !show}">
        <span>心灵鸡汤</span>
      </div>
      <div class="content-bg">{{bg_text[Math.floor(Math.random() * bg_text.length)]}}</div>
      <vue-particles
        color="#777"
        :particleOpacity="0.7"
        :particlesNumber="60"
        shapeType="circle"
        :particleSize="4"
        linesColor="#777"
        :linesWidth="1"
        :lineLinked="true"
        :lineOpacity="0.4"
        :linesDistance="150"
        :moveSpeed="2"
        :hoverEffect="true"
        hoverMode="grab"
        :clickEffect="true"
        clickMode="push"
        class="lizi"
      >
      </vue-particles>
      <div ref="scrollView" class="content" :class="{'content-anim': !show}">
        <div v-for="item, index in motto" :key="index" class="motto">
          <span>{{transformTime(item.create_at)}}</span>
          <span class="words">{{item.content}}</span>
          <span class="hx"><div></div></span>
          <span>{{item.author}}</span>
          <span class="esll">●●●</span>
        </div>
      </div>
    </div>
    <div class="bg-wrapper" :class="{'bg-wrapper-anim': !show}">
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
          <div class="read" @click="show = false"><span>读</span></div>
        </div>
      </div>
    </div>
    <div class="logo-wrapper">
      <a href="http://zcmol.cn">
        <div class="logo"></div>
      </a>
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
  import api from '../api/api'
  import PacmanLoader from "vue-spinner/src/ClipLoader";

  export default {
    name: 'motto',
    components: {PacmanLoader},
    data() {
      return {
        show: true,
        motto: [],
        bg_text: ['空·缘', '静·心', '无·非', '故·知'],
        paging: {
          current_idx: 1,
          has_next: false,
          has_prev: false,
          next_idx: null,
          prev_idx: null,
          total_pages: 1
        },
        per_page: 5,
        loading: true
      }
    },
    methods: {
      async getInitData(page, showLoading = true) {
        if (!page || page > this.paging.total_pages)
          return false
        if (showLoading)
          this.loading = true
        const result = await this.$$api(api.motto,
          {
            params: {
              page: page,
              per_page: this.per_page
            }
          })
        if (result.status !== 200) {
          alert('访问失败~')
          return false
        }
        this.loading = false
        this.motto = this.motto.concat(result.body.data.motto)
        this.paging = result.body.data.paging
      },
      transformTime(time) {
        return new Date(time).toLocaleDateString().replace(new RegExp('/', 'g'), '.')
      },
      // 滑动刷新
      scrollLoad() {
        this.viewBox = this.$refs.scrollView
        const self = this
        let func
        let can_visit = true
        this.viewBox.addEventListener('scroll', function () {
          if (func)
            clearTimeout(func)
          func = setTimeout(async () => {
            let scrollTop = self.viewBox.scrollTop
            let clientHeight = self.viewBox.clientHeight
            let allHeight = self.viewBox.scrollHeight
            if (scrollTop + clientHeight - allHeight <= 100) {
              if (can_visit) {
                can_visit = false
                await self.getInitData(self.paging.current_idx + 1, false)
                can_visit = true
              }
            }
          }, 200)
        }, false)
      }
    },
    async mounted() {
      document.title = '心灵鸡汤'
      await this.getInitData(1)
      this.scrollLoad()
    }
  }
</script>
