<style scoped lang="less">
  @import "../assets/my-style";

  @bo-color: #f6d76d;
  @bg-color: #f6d76d;
  @blue: #314e72;
  .full {
    background: url("../assets/loginbg.jpg") no-repeat;
    background-size: cover;
    background-position: 50%;
  }

  .wrap {
    width: 600px;
    height: 800px;
    position: relative;
    font-family: zcmol;
  }

  .avatar-div {
    height: 160px;
    width: 100%;
  }

  .avatar {
    height: 160px;
    width: 160px;
    border-radius: 80px;
    background-color: @bg-color;
    position: relative;
    top: -80px;
    @img-wh: 145px;
    img {
      height: @img-wh;
      width: @img-wh;
      border-radius: @img-wh;
    }
  }

  .login-wrap {
    width: 100%;
    height: 440px;
    border: 1px solid @bo-color;
    background-color: @bg-color;
    border-radius: 10px;
    position: relative;
    &::before {
      z-index: 10;
      position: absolute;
      content: "";
      width: 50px;
      height: 50px;
      border-width: 1px 0px 0px 1px;
      border-color: @bo-color;
      border-style: solid;
      top: -26px;
      margin-left: -26px;
      transform: rotate(45deg);
      background-color: @bg-color;
    }
  }

  .title {
    width: 100%;
    height: 60px;
    position: relative;
    top: 10px;
    margin-bottom: 20px;
    span {
      z-index: 11;
    }
  }
  .input-div {
    width: 100%;
    height: 60px;
    position: relative;
    margin-top: 40px;
    margin-bottom: 10px;
  }
  @out-color: #86cbdb;
  .input {
    font-size: 14px;
    width: 460px;
    height: 60px;
    border-radius: 5px;
    box-shadow: 3px 3px 5px #dfc111;
    &:focus {
      box-shadow: 0 0 5px 1px @out-color;
    }
  }
  .button {
    width: 460px;
    height: 60px;
    color: @white;
    background-color: @blue;
    border-radius: 10px;
    font-family: zcmol;
    &:hover {
      box-shadow: 0 0 5px 2px @out-color;
      cursor: pointer;
    }
    &:active{
      opacity: .9;
    }
  }
  .foot {
    position: relative;
    margin-top: 40px;
    font-family: zcmol;
    font-size: 24px;
    color: @bg-color;
  }
</style>

<template>
  <div class="full flex-mid">
    <div class="wrap">
      <div class="avatar-div flex-mid">
        <div class="avatar flex-mid">
          <img src="../assets/avater.jpg" alt="">
        </div>
      </div>
      <div class="login-wrap">
        <div class="title flex-mid font-bg">
          <span>{{app_name}}</span>
        </div>
        <div class="input-div flex-mid"><input v-model="username" type="text" class="input" placeholder="please enter username"></div>
        <div class="input-div flex-mid"><input v-model="password" type="password" class="input" placeholder="please enter password"></div>
        <div class="input-div flex-mid"><input type="button" class="button font30" value="Login" @click="login" /></div>
        <p class="font24">不知道密码的你，请离开吧~~</p>
      </div>
      <div class="foot">
        <p>@2016-2018 早茶月光, 无聊之人无聊之作</p>
      </div>
    </div>
  </div>
</template>

<script>
  import md5 from 'js-md5'
  import {app_name} from "../constant";

  export default {
    name: 'login',
    data () {
      return {
        app_name: app_name,
        username: "",
        password: ""
      }
    },
    methods: {
      login () {
        if (this.username === "") {
          alert("请输入用户名")
          return
        }
        if (this.password === "") {
          alert("请输入密码")
          return
        }
        const username = this.username
        const password = md5(md5(this.password))
        this.$router.push('/index')
      }
    }
  }
</script>















