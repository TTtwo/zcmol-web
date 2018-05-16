<style lang="less">
  @import "../assets/my-style";

  .wrapper {
    width: 100%;
    height: 100%;
    overflow: hidden;
    background-color: @white-gray;

    .header {
      width: 100%;
      height: 80px;
      background-color: @green-white;
      .flex(@horizontal: flex-start);
      .font-style(30px);

      .menu-btn {
        width: 80px;
        height: 80px;
        color: @red-org;
        margin-left: 40px;
        font-weight: bold;
        position: relative;
        .flex();

        &:hover {
          cursor: pointer;
        }
      }

      .title {
        color: @green;
        position: relative;
        margin-left: 20px;
        font-family: zcmol;
      }
    }

    .sub-wrapper {
      width: 100%;
      position: relative;
      height: calc(100% - 80px);
      transition: margin-left .5s ease-in-out;
      /*transition: width .5s ease-in-out;*/
      .mod {
        width: 100%;
        height: 100%;
        padding: 1px;
        overfow-y: scroll;

        .table {
          @marginLeft: 20px;

          .table-title {
            width: 100%;
            height: 70px;
            color: @white;
            font-size: 22px;
            position: relative;
            background-color: @green;
            div {
              float: left;
              height: 100%;
              position: relative;
              margin-left: @marginLeft;
              .flex(@horizontal: flex-start);
            }
          }

          .table-ul {
            width: 100%;

            li {
              width: 100%;
              height: 70px;
              font-size: 22px;
              position: relative;

              &:hover {
                cursor: pointer;
                background-color: @green-white;
              }
            }

            li > div {
              float: left;
              height: 100%;
              line-height: 70px;
              position: relative;
              margin-left: @marginLeft;
              .flex(@horizontal: flex-start);

              span {
                width: 100%;
                height: 100%;
                display: block;
                overflow: hidden;
                word-break: keep-all;
                text-overflow: ellipsis;
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
      top: 80px;
      width: 300px;
      position: absolute;
      margin-left: -300px;
      height: calc(100% - 80px);
      background-color: @black-blue;
      transition: margin-left .5s ease-in-out;
      .flex(@vertical: flex-start);

      .menu {
        top: 60px;
        width: 240px;
        position: relative;

        .sub-menu {
          width: 100%;
          color: @white;
          font-size: 24px;

          .sub-menu-title {
            width: 100%;
            height: 60px;
            position: relative;
            border-radius: 5px;
            .flex(@horizontal: space-between);

            &::before {
              top: 22px;
              right: 60px;
              width: 10px;
              height: 10px;
              content: "";
              position: absolute;
              border-style: solid;
              border-color: @white;
              transform: rotate(-135deg);
              border-width: 1px 0px 0px 1px;
              transition: all .5s ease-in-out;
            }

            &:hover {
              cursor: pointer;
              background-color: @green;
            }
          }

          .sub-menu-wrapper {
            width: 100%;
            max-height: 0px;
            overflow: hidden;
            position: relative;
            transform-origin: top;
            transition: max-height .2s ease-in-out;

            .sub-menu-txt {
              width: 100%;
              height: 60px;
              color: @white;
              font-size: 24px;
              .flex();

              &:hover {
                color: @green;
                cursor: pointer;
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

          .subMenuTitleAngerAnim {
            &::before {
              top: 26px;
              transform: rotate(45deg);
            }
          }
        }

        .span {
          display: inline-block;
        }
      }
    }

    .menuAnim {
      margin-left: 0px;
    }
  }

  .modal {

    .modal-item {
      margin-bottom: 15px;

      .modal-title {
        width: 100%;
        height: 60px;
        font-size: 24px;
        font-weight: bold;
        position: relative;
        border-radius: 5px;
        background-color: @green-white;
        .flex(@horizontal: flex-start);

        span {
          margin-left: 10px;
          position: relative;
        }
      }

      .modal-content {
        width: 100%;
        font-size: 24px;
        line-height: 44px;
        position: relative;
        background-color: @white-gray;

        span {
          display: block;
          padding: 0 10px;
        }
      }

      .modal-textarea {
        padding: 10px;
        display: block;
        .font-style(22px; @black);
        .base-textarea(@bsc: @green);
      }
    }
  }

</style>

<template>
  <div class="wrapper">
    <div class="header">
      <div class="menu-btn" @click="show_menu = !show_menu">=</div>
      <div class="title"><span>{{ app_name }}</span></div>
    </div>
    <div class="sub-wrapper" :class="{ subWrapperAnim: show_menu }">
      <router-view></router-view>
    </div>
    <div class="menu-wrapper" :class="{ menuAnim: show_menu }">
      <div class="menu">
        <div class="sub-menu" v-for="m,index in menus">
          <div class="sub-menu-title" :class="{ subMenuTitleAngerAnim: render_select_id === m.id }"
               @click="menusOpen(m)">
            <span class="span">{{ m.text }}</span>
          </div>
          <div class="sub-menu-wrapper" :class="{ openSubMenu: render_select_id === m.id }">
            <div class="sub-menu-txt" v-for="submenu in m.sub_menus"
                 :class="{ subMenuSelected: submenu.id === $route.name }"
                 @click="transformMenu(submenu.url)">
              {{ submenu.text }} ·
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

        const current = this.menus.filter(
          menu => menu.sub_menus.filter(
            sub => sub.id === this.$route.name
          ).length
        )

        if (current.length)
          return current[0].id

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
