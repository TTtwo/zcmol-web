<style scoped lang="less">
  @import "../assets/my-style";

  @bo-color: #f6d76d;
  @bg-color: #f6d76d;
  @blue: #314e72;
  .wrapper {
    height: 100%;
    width: 100%;
    background: url("../assets/loginbg.jpg") 50% no-repeat;
    background-size: cover;
    display: flex;
    justify-content: center;
    align-items: center;

    .sub-wrapper {
      width: 600px;
      height: 800px;
      position: relative;
      font-family: zcmol;

      .avatar-wrapper {
        height: 160px;
        width: 100%;
        .flex();

        .avatar {
          height: 160px;
          width: 160px;
          border-radius: 80px;
          background-color: @bg-color;
          position: relative;
          .flex();

          @img-wh: 145px;
          img {
            height: @img-wh;
            width: @img-wh;
            border-radius: @img-wh;
          }
        }
      }

      .login-wrapper {
        width: 100%;
        height: 440px;
        margin-top: 80px;
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

        .title {
          width: 100%;
          height: 60px;
          position: relative;
          top: 10px;
          margin-bottom: 20px;
          .flex();
          .font-style(30px; @black-blue);

          span {
            z-index: 11;
          }
        }
        .input-wrapper {
          width: 100%;
          height: 60px;
          position: relative;
          margin-top: 40px;
          margin-bottom: 10px;
          .flex();

          @out-color: #86cbdb;
          .input {
            .base-input(460px; 60px;)
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

            &:active {
              opacity: .9;
            }
          }

          p {
            .font-style(30px; @green-white)
          }
        }
      }
    }
  }

  .footer {
    position: relative;
    font-family: zcmol;
    font-size: 24px;
  }
</style>

<template>
  <div class="wrapper">
    <div class="sub-wrapper">
      <div class="avatar-wrapper">
        <div class="avatar">
          <img src="../assets/avater.jpg" alt="">
        </div>
      </div>
      <div class="login-wrapper">
        <div class="title">
          <span>{{ app_name }}</span>
        </div>
        <div class="input-wrapper"><input v-model="username" type="text" class="input"
                                          placeholder="please enter username"></div>
        <div class="input-wrapper"><input v-model="password" type="password" class="input"
                                          placeholder="please enter password"></div>
        <div class="input-wrapper"><input type="button" class="button" value="Login" @click="login"/>
        </div>
        <p>不知道密码的你，请离开吧~~</p>
      </div>
      <div class="footer">
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
    data() {
      return {
        app_name: app_name,
        username: "",
        password: ""
      }
    },
    methods: {
      login() {
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















