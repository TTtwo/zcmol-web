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
          background: url("../assets/logo.png") no-repeat center;
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
        transition: top .3s ease-in-out;
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
        <daily-comp class="content-page"></daily-comp>
        <about-me-comp class="content-page"></about-me-comp>
        <link-comp v-if="init_data" class="content-page" :links="init_data.links"></link-comp>
        <say-comp class="content-page"></say-comp>
        <guestbook-comp v-if="init_data" class="content-page" :guestbooks="init_data.guestbooks"></guestbook-comp>
      </div>
    </div>
    <div class="menu" :class="{'menu-anim': show_menu}" v-on:mouseleave="show_menu = false">
      <div class="menu-content">
        <div class="menu-btn" v-for="mu, index in menu" :title="mu.des" @click="mvMenuPosFunc(index)">{{ mu.name }}
        </div>
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

  export default {
    name: 'index',
    components: {DailyComp, GuestbookComp, LinkComp, AboutMeComp, SayComp},
    data() {
      return {
        menu: [
          {name: 'H', dis: "0%", des: '主界面'},
          {name: 'A', dis: "-100%", des: '关于我'},
          {name: 'L', dis: "-200%", des: '友链'},
          {name: 'S', dis: "-300%", des: '说说'},
          {name: 'G', dis: "-400%", des: '留言'},
          {name: 'B', dis: null, link: '', des: '博客文章, building...'},
          {name: 'M', dis: null, link: '#/motto', des: '心灵鸡汤'},
        ],
        menu_pos: 0,
        show_menu: false,
        init_data: null
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
        const result = await this.$$api(api.index, {})
        if (result.status !== 200) {
          this.$Message.error('访问失败~')
          return
        }
        this.init_data = result.body.data
        console.log(this.init_data.guestbooks)
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
