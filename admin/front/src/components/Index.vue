<style scoped lang="less">
  @import "../assets/my-style";

  .full {
    background-color: @white-gray;
    overflow: hidden;
  }

  .header {
    width: 100%;
    height: 80px;
    background-color: @green-white;
  }

  .title {
    position: relative;
    margin-left: 20px;
    color: @green;
    font-family: zcmol;
  }

  .menu-btn-div {
    height: 80px;
    width: 80px;
    font-weight: bold;
    position: relative;
    margin-left: 40px;
    color: @red-org;
    &:hover {
      cursor: pointer;
    }
  }

  .animation {
    transition: width .5s ease;
  }

  .menu {
    width: 300px;
    margin-left: -300px;
    transition: margin-left .5s ease-in-out;
    height: calc(100% - 80px);
    background-color: @black-blue;
    position: relative;
    float: left;
  }

  .menuAnim {
    margin-left: 0px;
  }

  .menu-div {
    position: relative;
    top: 60px;
    width: 240px;
  }

  .container {
    position: relative;
    height: calc(100% - 80px);
    width: 100%;
    transition: margin-left .5s ease-in-out;
    /*transition: width .5s ease-in-out;*/
  }

  .containerAnim {
    margin-left: 300px;
    /*width: calc(100% - 300px);*/
  }

  .menu-parent {
    width: 100%;
    color: @white;
    font-size: 24px;
  }

  .menu-parent-title {
    border-radius: 5px;
    width: 100%;
    height: 60px;
    position: relative;
    &::before {
      content: "";
      border-width: 1px 0px 0px 1px;
      border-style: solid;
      border-color: @white;
      transform: rotate(-135deg);
      position: absolute;
      top: 22px;
      right: 60px;
      width: 10px;
      height: 10px;
      transition: all .5s ease-in-out;
    }
    &:hover {
      background-color: @green;
      cursor: pointer;
    }
  }

  .menuOpen {
    &::before {
      top: 26px;
      transform: rotate(45deg);
    }
  }

  .span {
    display: inline-block;
  }

  .menu-sub-div {
    width: 100%;
    position: relative;
    overflow: hidden;
    max-height: 0px;
    transform-origin: top;
    transition: max-height .2s ease-in-out;
  }

  .menu-sub {
    width: 100%;
    height: 60px;
    font-size: 24px;
    color: @white;
    &:hover {
      cursor: pointer;
      color: @green;
    }
  }

  .menuSubOpen {
    /*transform: scale(1, 1);*/
    max-height: 300px;
  }

</style>

<template>
  <div class="full">
    <div class="header flex-mid left">
      <div class="font30 menu-btn-div flex-mid" @click="show_menu = !show_menu">=</div>
      <div class="font30 title"><span>{{ app_name }}</span></div>
    </div>
    <div class="menu flex-mid top" :class="{ menuAnim: show_menu}" @click="guestbook">
      <div class="menu-div">
        <div class="menu-parent" v-for="m,index in menus">
          <div class="menu-parent-title flex-mid left" :class="{menuOpen: select_id === m.id}" @click="menusOpen(m)">
            <span class="span">{{ m.text}}</span>
          </div>
          <div class="menu-sub-div" :class="{menuSubOpen: select_id === m.id}"
               v-for="submenu in m.sub_menus">
            <div class="menu-sub flex-mid">
              {{submenu.text}} ·
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container" :class="{ containerAnim: show_menu}">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import {app_name} from "../constant";

  export default {
    name: "index",
    data() {
      return {
        app_name: app_name,
        show_menu: false,
        select_id: -1,
        menus: [
          {
            id: 1,
            text: '评论管理',
            is_selected: false,
            sub_menus: [
              {
                id: 101,
                is_selected: false,
                text: '留言'
              },
              {
                id: 102,
                is_selected: false,
                text: '日志评论'
              }
            ]
          },
          {
            id: 2,
            text: '内容管理',
            is_selected: false,
            sub_menus: [
              {
                id: 201,
                is_selected: false,
                text: '写日志'
              },
              {
                id: 202,
                is_selected: false,
                text: '写说说'
              },
              {
                id: 203,
                is_selected: false,
                text: '写鸡汤'
              },
              {
                id: 204,
                is_selected: false,
                text: '写文章'
              }
            ]
          },
          {
            id: 3,
            text: '配    置',
            is_selected: false,
            sub_menus: [
              {
                id: 301,
                is_selected: false,
                text: '修改配置',
              }
            ]
          }
        ]
      }
    },
    methods: {
      menusOpen(m) {
        m.is_selected = !m.is_selected
        if (this.select_id === m.id) {
          this.select_id = -1
        } else {
          this.select_id = m.id
        }
      },
      guestbook () {
        this.$router.push('/guestbook')
      }
    }
  }
</script>
