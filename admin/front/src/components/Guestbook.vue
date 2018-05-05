<style scoped lang="less">
  @import "../assets/my-style";

  @media (max-width: 1024px) {
    .wrap {
      overflow: scroll;
    }
  }

  .table {
    width: 1370px;
    margin: auto;
    margin-top: 40px;
  }

  .table-header {
    width: 100%;
    height: 60px;
    position: relative;
    margin: 20px 0;
    span {
      height: 100%;
      position: relative;
      font-size: 22px;
      margin: 0 15px;
    }
  }
  .table-header-text {
    height: 100%;
    position: relative;
    background-color: @white;
    float: left;
  }
  .table-header-input {
    position: relative;
    float: left;
    width: 120px;
    height: 100%;
    > input {
      border: none;
      font-size: 24px;
      text-align: center;
      height: 100%;
      width: 100%;
      background-color: #c8c8c8;
      color: white;
      &::-webkit-input-placeholder {
        color: white;
        text-align: center;
      }
      &::-moz-placeholder {
        color: white;
        text-align: center;
      }
    }
  }
  .table-header-btn {
    height: 100%;
    position: relative;
    float: left;
    background-color: @white;
    &:hover {
      border: 1px solid @green-white;
      cursor: pointer;
    }
  }
  .ul {
    width: 100%;
    > li {
      width: 100%;
      height: 70px;
      position: relative;
      font-size: 22px;
      &:hover {
        cursor: pointer;
        background-color: @green-white;
      }
    }
    > li:first-child {
      background-color: @green;
      color: @white;
      &:hover {
        cursor: none;
      }
    }
    > li > div {
      position: relative;
      float: left;
      height: 70px;
      line-height: 70px;
      white-space: nowrap;
      margin-left: 20px;
    }
    .id {
      width: 30px;
    }
    .name {
      width: 160px;
    }
    .content {
      width: 300px;
    }
    .time {
      width: 220px;
    }
    .email {
      width: 240px;
    }
    .my-reply {
      width: 300px;
    }
    .span {
      text-overflow: ellipsis;
      overflow: hidden;
      word-break: keep-all;
      height: 100%;
      width: 100%;
    }
    .li-white {
      background-color: @white;
    }
  }

  .model-content-title {
    width: 100%;
    height: 60px;
    font-size: 24px;
    font-weight: bold;
    position: relative;
    background-color: @green-white;
    border-radius: 5px;
    > span {
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
    margin-bottom: 15px;
    line-height: 44px;
    > span {
      width: 100%;
      position: relative;
      margin-left: 10px;
    }
  }
  .model-btn-div {
    width: 100%;
    height: 80px;
    position: relative;
    margin-top: 30px;
  }
  .model-del-div {
    width: 220px;
    height: 60px;
    position: relative;
    margin-right: 20px;
    > input {
      width: 100%;
      height: 100%;
      font-size: 32px;
    }
  }


</style>

<template>
  <div class="wrap">
    <div class="table">
      <div class="table-header flex-mid left">
        <div class="table-header-text flex-mid"><span class="flex-mid">共3页 跳到</span></div>
        <div class="table-header-input"><input placeholder-style="color:white" type="text" class="input1" placeholder="输入页数"></div>
        <div class="table-header-btn"><span class="flex-mid">确定跳转</span></div>
      </div>
      <ul class="ul">
        <li>
          <div class="c-id flex-mid left">id</div>
          <div class="name flex-mid left">昵 称</div>
          <div class="time flex-mid left">时 间</div>
          <div class="content flex-mid left">内 容</div>
          <div class="email flex-mid left">邮 箱</div>
          <div class="my-reply flex-mid left">我的回复</div>
        </li>
        <li @click="change">
          <div class="c-id flex-mid left"><span class="span left">1</span></div>
          <div class="name flex-mid left"><span class="span left">我是小老拉时代峻峰拉水电费</span></div>
          <div class="time flex-mid left"><span class="span left">2018-06-03 12:55:12</span></div>
          <div class="content flex-mid left"><span class="span left">阿大山里的开发撒的浪费捡垃圾水电费炼金啊说的福利看手机对</span></div>
          <div class="email flex-mid left"><span class="span left">1297075993@qq.com</span></div>
          <div class="my-reply flex-mid left"><span class="span left">啊手动阀撒旦发爱上对方律师的阿斯顿立法局士大夫</span></div>
        </li>
      </ul>
      <Modal v-model="modal_show">
        <div class="model-content-title flex-mid left"><span class="flex-mid left">id</span></div>
        <div class="model-content"><span>1</span></div>
        <div class="model-content-title flex-mid left"><span class="flex-mid left">昵  称</span></div>
        <div class="model-content"><span>我是谁</span></div>
        <div class="model-content-title flex-mid left"><span class="flex-mid left">时  间</span></div>
        <div class="model-content"><span>2018-06-07 12:36:55</span></div>
        <div class="model-content-title flex-mid left"><span class="flex-mid left">内  容</span></div>
        <div class="model-content"><span>萨拉丁附件阿斯顿立法局阿斯蒂芬</span></div>
        <div class="model-content-title flex-mid left"><span class="flex-mid left">邮  箱</span></div>
        <div class="model-content"><span>1297075993@qq.com</span></div>
        <div class="model-content-title flex-mid left"><span class="flex-mid left">我的回复</span></div>
        <div class="model-content"><span>按时发送拉大锯拉萨的积分拉萨的空间</span></div>
        <div class="model-btn-div flex-mid right">
          <div class="model-del-div flex-mid">
            <input type="text" class="input1" placeholder="删除/修改"/>
          </div>
          <div class="btn1 flex-mid">
            删除
          </div>
          <div class="btn1 flex-mid">
            修改
          </div>
        </div>
      </Modal>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'guestbook',
    data() {
      return {
        modal_show: false
      }
    },
    methods: {
      change() {
        this.modal_show = true
      }
    }
  }
</script>




















