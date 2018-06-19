<style lang="less" scoped>
  @import "../../assets/my-style";

  #about-me {
    .info-wrapper {
      width: 40%;
      height: 100%;
      background-color: @green;
      overflow-y: scroll;
      position: relative;
      .title {
        padding-top: 20px;
        p {
          display: block;
          text-align: left;
          font-weight: bolder;
          padding-left: 20px;
          font-family: beleren;
          font-size: 60px;
          color: #333333;
        }
      }
      .des {
        padding: 20px 20px;
        .avatar {
          width: 160px;
          height: 160px;
          position: relative;
          float: left;
          img {
            width: 100%;
            height: 100%;
          }
        }
        .about {
          position: relative;
          padding-left: 150px;
          p {
            text-align: left;
            padding: 3px 20px 2px 40px;
            font-size: 18px;
            line-height: 36px;
          }
          .smh {
            padding-top: 5px;
            padding-bottom: 5px;
            color: #444444;
          }
        }
        &::after {
          content: '';
          display: block;
          visibility: hidden;
          height: 0;
          clear: both;
        }
      }
    }
    .contact-wrapper {
      position: absolute;
      left: 40%;
      right: 0;
      top: 0;
      bottom: 0;
      > div {
        height: 33.3%;
        width: 33.3%;
        border-left: 1px solid #333333;
        float: left;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
      }
      .show-im {
        background-color: @green;
        position: relative;
        .flex(@h: none);
        .imv {
          width: 100%;
          span {
            width: 100%;
            display: block;
            text-align: right;
            padding-right: 20px;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            font-family: beleren;
          }
          .text {
            font-size: 80px;
            color: #333333;
            line-height: 80px;
          }
          .textw {
            color: #333333;
            font-size: 18px;
            font-weight: bolder;
            line-height: 30px;
          }
          .job {
            font-size: 18px;
            color: #555555;
            font-weight: bolder;
          }
        }
      }
      .girl-bg {
        background: url("../../assets/two.png") no-repeat center;
        background-size: cover;
      }
      .contact {
        background-color: #313131;
        border-right: 1px solid #444;
        .flex;
        p {
          display: inline-block;
          font-size: 50px;
          color: #777;
          font-family: beleren;
        }
        &:hover {
          cursor: pointer;
          background-color: #d78893;
          p {
            color: #333333;
          }
        }
      }
    }
  }
</style>

<template>
  <div id="about-me">
    <div class="info-wrapper">
      <div class="title">
        <p>About</p>
        <p>Me</p>
      </div>
      <dl class="des">
        <dt class="avatar"><img src="../../assets/Icon1.png"></dt>
        <dd class="about">
          <p>昵称：早茶月光</p>
          <p>年龄：？？</p>
          <p>性别：男</p>
          <p>职业：游戏开发(打酱油)</p>
          <p>爱好：编程，音乐，篮球，阅读</p>
          <p>Detail</p>
          <p class="smh">-关于此博客</p>
          <p>
            网站风格是模仿大神的&nbsp;(&nbsp;虽然模仿别人的感觉不好，但是偶尔充满罪恶感还是让生活增加趣味的~~&nbsp;)
          </p>
          <p class="smh">-待人</p>
          <p>缘深多聚聚，缘浅随它去</p>
        </dd>
      </dl>
    </div>
    <div class="contact-wrapper">
      <div class="show-im">
        <div class="imv">
          <span class="text">I'm</span>
          <span class="textw">Mr.Feng</span>
          <span class="textw">早茶月光</span>
          <span class="job">Game Programmer</span>
        </div>
      </div>
      <div class="girl-bg"></div>
      <div class="contact"></div>
      <div class="contact"></div>
      <div class="contact">
        <p>
          code<br>
          source
        </p>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'aboutMe'
  }
</script>
