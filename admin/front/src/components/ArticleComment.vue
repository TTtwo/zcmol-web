<style scoped lang="less">
  @import "../assets/my-style";

  .table {
    width: 1370px;
    margin: auto;
    margin-top: 40px;
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
    .article {
      width: 180px;
    }
    .name {
      width: 180px;
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

  .model-reply-div {
    width: 100%;
    height: 160px;
    position: relative;
    border: 1px solid @black-blue;
    border-radius: 5px;
    > textarea {
      width: 100%;
      height: 100%;
      position: relative;
      border-radius: 5px;
      font-size: 24px;
      resize: none;
      padding-left: 10px;
      padding-right: 10px;
    }
  }
</style>

<template>
  <div class="wrap">
    <div class="table">
      <ul class="ul">
        <li>
          <div class="article flex-mid left">日 志</div>
          <div class="name flex-mid left">昵 称</div>
          <div class="time flex-mid left">时 间</div>
          <div class="content flex-mid left">内 容</div>
          <div class="email flex-mid left">邮 箱</div>
        </li>
        <li @click="change">
          <div class="article flex-mid left"><span class="span-mid left">结束不过开始</span></div>
          <div class="name flex-mid left"><span class="span left">我是小老拉时代峻峰拉水电费</span></div>
          <div class="time flex-mid left"><span class="span left">2018-06-03 12:55:12</span></div>
          <div class="content flex-mid left"><span class="span left">阿大山里的开发撒的浪费捡垃圾水电费炼金啊说的福利看手机对</span></div>
          <div class="email flex-mid left"><span class="span left">1297075993@qq.com</span></div>
        </li>
      </ul>
      <page-comp></page-comp>
      <Modal v-model="modal_show">
        <div class="model-content-title flex-mid left"><span class="flex-mid left">id</span></div>
        <div class="model-content"><span>1</span></div>
        <div class="model-content-title flex-mid left"><span class="flex-mid left">昵  称</span></div>
        <div class="model-content"><span>我是谁</span></div>
        <div class="model-content-title flex-mid left">回复的人</div>
        <div class="model-content flex-mid left">傻傻不快乐</div>
        <div class="model-content-title flex-mid left">回复的人的评论</div>
        <div class="model-content flex-mid left">id:1 你就是个傻逼</div>
        <div class="model-content-title flex-mid left"><span class="flex-mid left">回复内容</span></div>
        <div class="model-content"><span>萨拉丁附件阿斯顿立法局阿斯蒂芬</span></div>
        <div class="model-btn-div flex-mid right">
          <div class="model-del-div flex-mid">
            <input type="text" class="input1" placeholder="删除/修改/回复"/>
          </div>
          <div class="btn1 flex-mid">
            删除
          </div>
          <div class="btn1 flex-mid">
            修改
          </div>
          <div class="btn1 flex-mid">回复</div>
        </div>
        <div class="model-reply-div">
          <textarea name="myreply" id="mrp" cols="30" rows="10">

          </textarea>
        </div>
      </Modal>
    </div>
  </div>
</template>

<script>
  import PageComp from './PagingComponent'
  export default {
    name: 'articleComment',
    components: { PageComp },
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



















