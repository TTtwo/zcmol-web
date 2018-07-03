<style lang="less" scoped>
  @import "../../assets/my-style";

  #links {
    .link-tip {
      background-color: @green;
      height: 200px;
      width: 600px;
      border-bottom: 1px solid #3a3a3a;
      div {
        position: relative;
        float: left;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
        width: 50%;
        height: 100%;
      }
      .link-tip-text {
        p {
          text-align: right;
          padding-right: 20px;
        }
        .text {
          padding-top: 20px;
          font-size: 60px;
          font-family: beleren;
        }
        .words {
          font-weight: bolder;
          font-size: 16px;
          padding-bottom: 5px;
        }
        .tex {
          font-size: 16px;
          padding-bottom: 5px;
        }
      }
      .link-btn {
        .flex;
        div {
          background-color: #333;
          width: 120px;
          height: 3px;
          position: absolute;
          transition: width .1s ease-in-out;
        }
        .ver {
          transform: rotate(90deg);
        }
        &:hover .ver, &:hover .hor {
          width: 140px;
        }
        &:hover {
          cursor: pointer;
        }
      }
    }
    .link-wrapper {
      width: 100%;
      height: calc(100% - 200px);
      overflow-y: scroll;
      .link-ul {
        list-style: none;
        .li-item {
          position: relative;
          border-right: 2px solid #222;
          float: left;
          color: #333333;
          .link-name {
            padding: 30px 40px;
            background-color: @green;
            .flex(@h: space-around);
            .add {
              font-size: 80px;
              width: 40px;
              height: 40px;
              overflow: hidden;
              .flex;
            }
            .text {
              font-size: 40px;
              padding-left: 20px;
              &:hover {
                color: #666;
              }
            }
          }
          .link-url {
            width: 100%;
            height: 50px;
            background-color: #3a3a3a;
            position: relative;
            -webkit-box-shadow: 0 0 5px #3a3a3a;
            -moz-box-shadow: 0 0 5px #3a3a3a;
            box-shadow: 0 0 5px #3a3a3a;
            &::before {
              content: '';
              width: 20px;
              height: 20px;
              border-top: 1px solid #3a3a3a;
              border-left: 1px solid #3a3a3a;
              transform: rotate(45deg);
              background-color: #3a3a3a;
              position: absolute;
              left: 48px;
              top: -8px;
              border-radius: 5px;
              -webkit-box-shadow: 0 0 5px #3a3a3a;
              -moz-box-shadow: 0 0 5px #3a3a3a;
              box-shadow: 0 0 5px #3a3a3a;
            }
            .flex;
            span {
              color: #888;
              -webkit-box-sizing: border-box;
              -moz-box-sizing: border-box;
              box-sizing: border-box;
              padding: 2px 4px;
              font-size: 20px;
              font-family: beleren;
            }
          }
        }
        &::after {
          content: '';
          height: 0;
          visibility: hidden;
          display: block;
          clear: both;
        }
      }
    }
  }
</style>
<template>
  <div id="links">
    <div class="link-tip">
      <div class="link-tip-text">
        <p class="text">Links</p>
        <p class="words">天地之间巧逢君</p>
        <p class="tex">做个简单的朋友，来？</p>
        <p class="tex">点击右边申请 ></p>
      </div>
      <div class="link-btn">
        <div class="ver"></div>
        <div class="hor"></div>
      </div>
    </div>
    <div class="link-wrapper">
      <ul class="link-ul">
        <li v-for="item, index in link_array" :key='index' class="li-item">
          <div class="link-name">
            <p class="add">+</p>
            <a :href="item.url" target="_blank" class="text">{{item.name}}</a>
          </div>
          <div class="link-url"><span>{{item.url}}</span></div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'links',
    props: ['links'],
    data() {
      return {
        link_array: this.links
      }
    }
  }
</script>
