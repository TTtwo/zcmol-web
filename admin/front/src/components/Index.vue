<style lang="less">
  @import "../assets/my-style";

  .wrapper {
    width: 100%;
    height: 100%;
    background-color: @white-gray;
    overflow: hidden;
    .header {
      width: 100%;
      height: 80px;
      background-color: @green-white;
      .flex-mid;
      .left;
      .font30;
      .menu-btn {
        height: 80px;
        width: 80px;
        font-weight: bold;
        position: relative;
        margin-left: 40px;
        color: @red-org;
        .flex-mid;
        &:hover {
          cursor: pointer;
        }
      }
      .title {
        position: relative;
        margin-left: 20px;
        color: @green;
        font-family: zcmol;
      }
    }

    .sub-wrapper {
      position: relative;
      height: calc(100% - 80px);
      width: 100%;
      transition: margin-left .5s ease-in-out;
      /*transition: width .5s ease-in-out;*/
      .mod {
        width: 100%;
        height: 100%;
        overflow-y: scroll;
        .table {
          @marginLeft: 20px;
          .table-title {
            width: 100%;
            height: 70px;
            position: relative;
            font-size: 22px;
            background-color: @green;
            color: @white;
            div {
              height: 100%;
              margin-left: @marginLeft;
              position: relative;
              float: left;
              display: flex;
              align-items: center;
              justify-self: flex-start;
            }
          }
          .table-ul {
            width: 100%;
            li {
              width: 100%;
              height: 70px;
              position: relative;
              font-size: 22px;
              &:hover {
                cursor: pointer;
                background-color: @green-white;
              }
            }
            li > div {
              position: relative;
              float: left;
              height: 100%;
              line-height: 70px;
              margin-left: @marginLeft;
              display: flex;
              align-items: center;
              justify-content: flex-start;
              span {
                display: block;
                text-overflow: ellipsis;
                overflow: hidden;
                word-break: keep-all;
                height: 100%;
                width: 100%;
              }
            }
          }
        }
        @media (max-width: 1024px) {
          .wrap {
            overflow: scroll;
          }
        }
        .modal {
          .modal-wrapper {
            margin-bottom: 15px;
            .modal-title {
              width: 100%;
              height: 60px;
              font-size: 24px;
              font-weight: bold;
              position: relative;
              background-color: @green-white;
              border-radius: 5px;
              display: flex;
              align-items: center;
              justify-content: flex-start;
              span {
                height: 100%;
                position: relative;
                margin-left: 10px;
              }
            }
            .model-content {
              width: 100%;
              position: relative;
              font-size: 24px;
              background-color: @white-gray;
              line-height: 44px;
              span {
                width: 100%;
                position: relative;
                margin-left: 10px;
              }
            }
          }
        }
      }
    }
    .subWrapperAnim {
      margin-left: 300px;
      /*width: calc(100% - 300px);*/
    }

    .menu-wrapper {
      width: 300px;
      margin-left: -300px;
      transition: margin-left .5s ease-in-out;
      height: calc(100% - 80px);
      background-color: @black-blue;
      position: absolute;
      top: 80px;
      .flex-mid;
      .top;
      .menu {
        position: relative;
        top: 60px;
        width: 240px;
        .sub-menu {
          width: 100%;
          color: @white;
          font-size: 24px;
          .sub-menu-title {
            border-radius: 5px;
            width: 100%;
            height: 60px;
            position: relative;
            .flex-mid;
            .left;
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
          .sub-menu-wrapper {
            width: 100%;
            position: relative;
            overflow: hidden;
            max-height: 0px;
            transform-origin: top;
            transition: max-height .2s ease-in-out;
            .sub-menu-txt {
              width: 100%;
              height: 60px;
              font-size: 24px;
              color: @white;
              &:hover {
                cursor: pointer;
                color: @green;
              }
            }
            .subMenuSelected {
              color: @green;
            }
          }
          .openSubMenu {
            /*transform: scale(1, 1);*/
            max-height: 300px;
          }
        }
        .span {
          display: inline-block;
        }
      }
      .openMenu {
        &::before {
          top: 26px;
          transform: rotate(45deg);
        }
      }
    }
    .menuAnim {
      margin-left: 0px;
    }
  }

</style>

<template>
  <div class="wrapper">
    <div class="header">
      <div class="menu-btn" @click="show_menu = !show_menu">=</div>
      <div class="title"><span>{{ app_name }}</span></div>
    </div>
    <div class="sub-wrapper" :class="{ subWrapperAnim: show_menu}">
      <router-view></router-view>
    </div>
    <div class="menu-wrapper" :class="{ menuAnim: show_menu}">
      <div class="menu">
        <div class="sub-menu" v-for="m,index in menus">
          <div class="sub-menu-title" :class="{openMenu: render_select_id === m.id}"
               @click="menusOpen(m)">
            <span class="span">{{ m.text}}</span>
          </div>
          <div class="sub-menu-wrapper" :class="{openSubMenu: render_select_id === m.id}"
               v-for="submenu in m.sub_menus">
            <div class="sub-menu-txt" :class="{subMenuSelected: submenu.id === $route.name}"
                 @click="transformMenu(submenu.url)">
              {{submenu.text}} ·
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {app_name, menus} from "../constant";

  export default {
    name: "index",
    data() {
      return {
        app_name: app_name,
        show_menu: false,
        select_id: -1,
        menus: menus
      }
    },
    computed: {
      render_select_id() {
        if (this.select_id !== -1)
          return this.select_id

        const current = this.menus.filter(menu => menu.sub_menus.filter(sub => sub.id === this.$route.name).length)
        if (current.length)
          return current[0].id
        else
          return -1
      }
    },
    methods: {
      transformMenu(url) {
        this.$router.push(url)
      },
      menusOpen(m) {
        this.select_id = m.id
      }
    }
  }
</script>
