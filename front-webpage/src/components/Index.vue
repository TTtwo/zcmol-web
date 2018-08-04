<style scoped lang="less">
  @import "../assets/my-style";

  #index {
    width: 100%;
    height: 100%;
    background: url("../assets/bg.gif") repeat;
    overflow: hidden;
    .header {
      height: 25%;
      position: relative;
      .logo-wrapper {
        width: 30%;
        height: 100%;
        position: relative;
        float: left;
        .flex(@h: flex-start);

        .logo {
          width: 100%;
          height: 100%;
          max-height: 196px;
          max-width: 256px;
          background: url("../../static/logo.png") no-repeat center;
          background-size: contain;
        }
      }
      .open-menu {
        width: 120px;
        height: 100%;
        position: relative;
        background: url("../assets/btn.png") no-repeat center;
        float: right;
        left: 0;
        margin-right: 80px;
        transition: left .3s ease-in-out;
        &:hover {
          cursor: pointer;
        }
      }
      .open-menu-anim {
        left: -108px;
      }
    }
    .container {
      position: relative;
      width: 100%;
      height: 75%;
      overflow: hidden;
      left: 0;
      transition: left .3s ease-in-out;
      .content-wrapper {
        width: 100%;
        height: 400%;
        top: 0;
        position: relative;
        transition: top .2s ease-in-out;
        .content-page {
          height: 25%;
          width: 100%;
          position: relative;
        }
      }
    }
    .container-anim {
      left: -108px;
    }
    .menu {
      height: 100%;
      background-color: @green;
      width: 108px;
      position: absolute;
      top: 0;
      right: -108px;
      transition: right .3s ease-in-out;
      font-family: beleren;
      .flex(@v: flex-start);
      .menu-content {
        width: 100%;
        position: relative;
        margin-top: 20px;
        .menu-btn {
          height: 100px;
          line-height: 80px;
          width: 100%;
          font-size: 80px;
          color: #222;
          overflow: hidden;
          position: relative;
          padding: 15px 0;
          -webkit-box-sizing: border-box;
          -moz-box-sizing: border-box;
          box-sizing: border-box;
          &:hover {
            cursor: pointer;
            background-color: #ff9ca9;
          }
        }
      }
    }
    .menu-anim {
      transition: right .3s ease-in-out .1s;
      right: 0px;
    }
    @media (max-width: 1024px) {
      .header {
        height: 20%;
      }

      .container {
        height: 80%;
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
    .i-music {
      position: absolute;
      top: 25%;
      left: 0;
      transition: left .5s ease-in-out;
      .flex;
      .m-close {
        width: 35px;
        height: 50px;
        background: #cce8cf url("../assets/lefts.png") no-repeat center;
        transform: rotate(180deg);
        transition: transform .5s ease-in-out;
        background-size: 30%;
        position: relative;
        left: -7px;
        &:hover {
          cursor: pointer;
        }
      }
      .m-close-anim {
        transform: rotate(0);
      }
    }
  }
</style>

<template>
  <div id="index">
    <div class="header">
      <div class="logo-wrapper">
        <div class="logo"></div>
      </div>
      <div class="open-menu" @click="show_menu = !show_menu" :class="{'open-menu-anim': show_menu}"></div>
    </div>
    <div class="container" :class="{'container-anim': show_menu}">
      <div class="content-wrapper" :style="{top: mvMenuPos}">
        <daily-comp class="content-page" :daily="init_data.daily"></daily-comp>
        <about-me-comp class="content-page"></about-me-comp>
        <link-comp class="content-page" @gu="mvMenuPosFunc" :links="init_data.links"></link-comp>
        <say-comp class="content-page"></say-comp>
        <guestbook-comp class="content-page" :guestbooks="init_data.guestbooks"></guestbook-comp>
      </div>
    </div>
    <div class="menu" :class="{'menu-anim': show_menu}" v-on:mouseleave="show_menu = false">
      <div class="menu-content">
        <div class="menu-btn" v-for="mu, index in menu" :title="mu.des" @click="mvMenuPosFunc(index)">{{ mu.name }}
        </div>
      </div>
    </div>
    <div ref="imusic" class="i-music">
      <aplayer
        autoplay
        :theme="'#222222'"
        :list="list3"
        :music="list3[0]"
      />
      <div class="m-close" :class="{'m-close-anim': !music_show}" @click="musicHidden"></div>
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
  import DailyComp from './common/DailyComponent'
  import GuestbookComp from './common/GuestbookComponent'
  import LinkComp from './common/LinkComponent'
  import AboutMeComp from './common/AboutMeComponent'
  import SayComp from './common/SayComponent'
  import api from '../api/api'
  import PacmanLoader from "vue-spinner/src/ClipLoader";
  import Aplayer from 'vue-aplayer'

  export default {
    name: 'index',
    components: {Aplayer, PacmanLoader, DailyComp, GuestbookComp, LinkComp, AboutMeComp, SayComp},
    data() {
      return {
        menu: [
          {name: 'H', dis: "0%", des: '主界面'},
          {name: 'A', dis: "-100%", des: '关于我'},
          {name: 'L', dis: "-200%", des: '友链'},
          {name: 'S', dis: "-300%", des: '说说'},
          {name: 'G', dis: "-400%", des: '留言'},
          {name: 'B', dis: null, link: '', des: '博客文章, building...'},
          {name: 'M', dis: null, link: '/motto', des: '心灵鸡汤'},
        ],
        menu_pos: 0,
        show_menu: false,
        init_data: {
          daily: [],
          links: [],
          guestbooks: []
        },
        loading: true,
        list3: [
          {
            title: '视线所及只剩生活',
            artist: '蔡维泽',
            src: 'http://zcmol-1253645803.file.myqcloud.com/music/sxsjzssh.mp3',
          },
          {
            title: '新年未老',
            artist: '许含光',
            src: 'http://zcmol-1253645803.file.myqcloud.com/music/xnwl.mp3',
          },
          {
            title: '9420',
            artist: '麦小兜',
            src: 'http://zcmol-1253645803.file.myqcloud.com/music/9420.mp3',
          },
          {
            title: '漆黑',
            artist: '朴信惠',
            src: 'http://zcmol-1253645803.file.myqcloud.com/music/%E6%9C%B4%E4%BF%A1%E6%83%A0%20-%20%E6%BC%86%E9%BB%91.mp3',
          }
        ],
        music_show: false
      }
    },
    methods: {
      mvMenuPosFunc(index) {
        const item = this.menu[index]
        if (item.dis != null) {
          this.menu_pos = item.dis
        }
        else if (item.link) {
          window.open(window.location.origin + item.link)
        }
      },
      async getInitData() {
        this.loading = true
        const result = await this.$$api(api.index, {})
        if (result.status !== 200) {
          alert('访问失败~')
          return
        }
        this.init_data = result.body.data
        this.loading = false
      },
      musicHidden() {
        this.music_show = !this.music_show
        let left = 0
        if (this.music_show)
          left = -(this.$refs.imusic.offsetWidth - 28)
        this.$refs.imusic.style.left = left + 'px'
      }
    },
    computed: {
      mvMenuPos() {
        return this.menu_pos
      }
    },
    mounted() {
      this.getInitData()
    }
  }
</script>
