<style scoped lang="less">
  @import "../assets/my-style.less";

  #love-game {
    width: 100vw;
    height: 100vh;
    background-color: #333333;
    .wrap {
      width: 100%;
      height: 100%;
      .flex;
      position: relative;

      .one {
        position: relative;
        width: 80%;
        height: 400px;
        border: 1px solid white;
        box-shadow: 0 0 5px white;
        border-radius: 10px;
        background: url("../assets/bg.gif");
        .close-wrap {
          width: 80px;
          height: 80px;
          position: absolute;
          right: 10px;
          top: 10px;
          .flex;
          .c-zero {
            width: 70px;
            height: 1px;
            background-color: white;
            position: absolute;
          }
          .c-one {
            -webkit-transform: rotate(45deg);
            -moz-transform: rotate(45deg);
            -ms-transform: rotate(45deg);
            -o-transform: rotate(45deg);
            transform: rotate(45deg);
          }
          .c-two {
            -webkit-transform: rotate(-45deg);
            -moz-transform: rotate(-45deg);
            -ms-transform: rotate(-45deg);
            -o-transform: rotate(-45deg);
            transform: rotate(-45deg);
          }
          &:hover {
            cursor: pointer;
            opacity: .5;
          }
        }
        .peiTu {
          position: absolute;
          top: 60px;
          left: calc(50% - 250px);
          img {
            width: 200px;
            max-height: 240px;
          }
        }
        .say {
          font-size: 40px;
          color: white;
          position: absolute;
          top: 100px;
          left: 50%;
          max-width: 300px;
          text-align: left;
          text-indent: 2em;
        }
        .btn {
          width: 150px;
          height: 60px;
          background-color: white;
          color: #000;
          font-size: 40px;
          position: absolute;
          .flex;
          bottom: 20px;
          &:hover {
            cursor: pointer;
            opacity: .5;
          }
        }
        .btn1 {
          left: calc(50% - 170px);
        }
        .btn2 {
          right: calc(50% - 170px);
        }
      }

    }
    .wrap1 {
      width: 100%;
      height: 100%;
      position: relative;
      top: -100%;
      .flex;
      .wrap1-bg {
        width: 100%;
        height: 100%;
        position: absolute;
        background-color: black;
        opacity: .5;
      }
      .two {
        top: -100px;
        position: relative;
        width: 80%;
        height: 400px;
        border: 1px solid white;
        box-shadow: 0 0 5px white;
        border-radius: 10px;
        background: url("../assets/bg.gif");
        .peiTu {
          position: absolute;
          top: 40px;
          left: calc(50% - 250px);
          img {
            width: 200px;
            max-height: 240px;
          }
        }
        .say {
          font-size: 40px;
          color: white;
          position: absolute;
          top: 80px;
          left: 50%;
          max-width: 300px;
          text-align: left;
          text-indent: 2em;
        }
        .btn {
          width: 150px;
          height: 60px;
          background-color: white;
          color: #000;
          font-size: 40px;
          position: absolute;
          .flex;
          bottom: 40px;
          &:hover {
            cursor: pointer;
            opacity: .5;
          }
        }
        .btn1 {
          left: calc(50% - 170px);
        }
        .btn2 {
          right: calc(50% - 170px);
        }
      }
    }
  }

</style>
<template>
  <div id="love-game">
    <div class="wrap">
      <div class="one">
        <div class="close-wrap" @click="close">
          <div class="c-zero c-one"></div>
          <div class="c-zero c-two"></div>
        </div>
        <div class="peiTu">
          <img :src="selOne.url" alt="">
        </div>
        <div class="say">
          {{selOne.desc}}
        </div>
        <div class="btn btn1" @click="agree">{{selOne.yes}}</div>
        <div class="btn btn2" @click="notAgree">{{selOne.no}}</div>
      </div>
    </div>
    <div class="wrap1" v-show="showTwo">
      <div class="wrap1-bg"></div>
      <div class="two">
        <div class="peiTu">
          <img :src="selTwo.url" alt="">
        </div>
        <div class="say">
          {{selTwo.desc}}
        </div>
        <div class="btn btn1" @click="twoHidden">{{selTwo.yes}}</div>
        <div class="btn btn2" @click="twoHidden">{{selTwo.no}}</div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'love-game',
    data() {
      return {
        showTwo: false,
        times: 0,
        words: [],
        closeWords: [
          {
            url: 'http://zcmol-1253645803.file.myqcloud.com/loveGame/2.jpg',
            desc: '我妈会游泳，你真的不考虑下？',
            yes: '哇, 嗯嗯',
            no: '考虑'
          },
          {
            url: '',
            desc: '我也会游泳，难道还不够吸引？',
            yes: '很吸引~',
            no: '考虑'
          }
        ],
        closeIndex: 0,
        selOne: {
          url: 'http://zcmol-1253645803.file.myqcloud.com/loveGame/1.jpg',
          desc: '我是从抖音看回来的，你信吗？',
          yes: '信',
          no: '不信',
        },
        selTwo: {},
      }
    },
    methods: {
      agree() {
        if (this.times === 0) {
          this.selTwo = {
            url: 'http://zcmol-1253645803.file.myqcloud.com/loveGame/3.jpg',
            desc: '姑娘，信的这么快，乱来的吧？',
            yes: '对的',
            no: '好像是'
          };
          this.showTwo = true;
          return;
        }
      },
      notAgree() {
      },
      close() {
        this.selTwo = this.closeWords[this.closeIndex];
        this.closeIndex = (this.closeIndex + 1) % this.closeWords.length
        this.showTwo = true;
      },
      twoHidden() {
        this.showTwo = false;
      }
    }
  }
</script>
