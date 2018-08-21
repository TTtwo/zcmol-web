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
            height: 5px;
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
        .say-say {
          left: 30%;
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
        <div class="close-wrap" v-show="canClick" @click="close">
          <div class="c-zero c-one"></div>
          <div class="c-zero c-two"></div>
        </div>
        <div class="peiTu">
          <img :src="selOne.url" alt="">
        </div>
        <div class="say" :class="{'say-say': this.laseClick}" v-html="selOne.desc">
          {{selOne.desc}}
        </div>
        <div class="btn btn1" v-show="!laseClick" @click="agree">{{selOne.yes}}</div>
        <div class="btn btn2" v-show="canClick" @click="close">{{selOne.no}}</div>
      </div>
    </div>
    <div class="wrap1" v-show="showTwo">
      <div class="wrap1-bg"></div>
      <div class="two">
        <div class="peiTu">
          <img :src="selTwo.url" alt="">
        </div>
        <div class="say" v-html="selTwo.desc">
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
    name: 'love_game',
    data() {
      return {
        showTwo: false,
        canClick: true,
        laseClick: false,
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
            url: 'http://zcmol-1253645803.file.myqcloud.com/loveGame/5.jpg',
            desc: "<span style='color: red; font-size:18px'>请你不要拒绝我!</span>",
            yes: '回心',
            no: '转意'
          },
          {
            url: 'http://zcmol-1253645803.file.myqcloud.com/loveGame/6.jpeg',
            desc: "<span style='color: lawngreen;font-size: 20px;'>房产证写你名字( • ̀ω•́ )✧</span>",
            yes: '心动',
            no: '考虑'
          },
          {
            url: 'http://zcmol-1253645803.file.myqcloud.com/loveGame/7.jpg',
            desc: "这辈子都不可能让你离开我(｡◕ˇ∀ˇ◕)",
            yes: '在一起',
            no: '一起'
          },
          {
            url: 'http://zcmol-1253645803.file.myqcloud.com/loveGame/8.jpg',
            desc: "<span style='color: red; font-size: 16px'>你没的选了,  </span>你只能选择好了~(*￣︶￣)~",
            yes: '接受',
            no: '接受'
          }
        ],
        closeIndex: 0,
        selOne: {
          url: 'http://zcmol-1253645803.file.myqcloud.com/loveGame/4.jpeg',
          desc: "<span style='color: #888888; font-size: 16px;'>小姐姐，观察你很久了</span>&nbsp;&nbsp;做我女朋友好不好?",
          yes: '好',
          no: '不好',
        },
        selTwo: {},
      }
    },
    methods: {
      async agree() {
        if (this.times === 0) {
          this.selTwo = {
            url: 'http://zcmol-1253645803.file.myqcloud.com/loveGame/3.jpg',
            desc: "<span style='color: #888888; font-size: 14px'>答应的太快了，你再好好想想呗~</span>&nbsp;&nbsp;有点开心O(∩_∩)O",
            yes: '嗯嗯',
            no: '好的'
          };
          this.showTwo = true;
          return;
        }
        this.selOne = {
          url: '',
          desc: "是你说做我女朋友的哦，答应了可不许后悔(ﾉ≧∀≦)ﾉ <span style='color: red; font-size: 14px;'><br>自行左上角关闭</span>",
          yes: '',
          no: '',
        }
        this.laseClick = true;
        this.canClick = false;
      },
      close() {
        this.selTwo = this.closeWords[this.closeIndex];
        this.times++
        this.closeIndex = (this.closeIndex + 1) % this.closeWords.length
        this.showTwo = true;
      },
      twoHidden() {
        if (this.times >= this.closeWords.length) {
          this.canClick = false;
        }
        this.showTwo = false;
      }
    }
  }
</script>
