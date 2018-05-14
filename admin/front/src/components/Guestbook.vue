<style scoped lang="less">
  @import "../assets/my-style";

  .mod {
    .table {
      width: 1370px;
      margin: auto;
      margin-top: 40px;
    }
    .modal {
      .modal-btn-wrapper {
        width: 100%;
        height: 80px;
        position: relative;
        margin-top: 30px;
        .flex-mid;
        .right;
        .modal-input-wrapper {
          width: 220px;
          height: 60px;
          position: relative;
          margin-right: 20px;
          .flex-mid;
          input {
            width: 100%;
            height: 100%;
            font-size: 32px;
          }
        }
      }
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
  }


</style>

<template>
  <div class="mod">
    <div class="table">
      <div class="table-title">
        <div class="id">id</div>
        <div class="name">昵 称</div>
        <div class="time">时 间</div>
        <div class="content">内 容</div>
        <div class="email">邮 箱</div>
        <div class="my-reply">我的回复</div>
      </div>
      <ul class="table-ul">
        <li @click="change">
          <div class="id"><span>1</span></div>
          <div class="name"><span>我是小老拉时代峻峰拉水电费</span></div>
          <div class="time"><span>2018-06-03 12:55:12</span></div>
          <div class="content"><span>阿大山里的开发撒的浪费捡垃圾水电费炼金啊说的福利看手机对</span></div>
          <div class="email"><span>1297075993@qq.com</span></div>
          <div class="my-reply"><span>啊手动阀撒旦发爱上对方律师的阿斯顿立法局士大夫</span></div>
        </li>
      </ul>
    </div>
    <page-comp></page-comp>
    <Modal v-model="modal_show" class="modal">
      <div class="modal-wrapper" v-for="(item, key) in modal_data" :key="key">
        <div class="modal-title"><span class="flex-mid left">{{ modalKeyText[key] }}</span></div>
        <div class="modal-content"><span> {{ item }}</span></div>
      </div>
      <div class="modal-btn-wrapper">
        <div class="modal-input-wrapper">
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
</template>

<script>
  import PageComp from './common/PagingComponent'
  import {MODALKEYTEXT} from '../constant'

  export default {
    name: 'guestbook',
    components: {PageComp},
    data() {
      return {
        modalKeyText: MODALKEYTEXT,
        modal_show: false,
        modal_data: {
          id: 1,
          nickName: 'TTtwo',
          time: '2016 11 11',
          content: '巴拉巴拉',
          email: '12465464@qq.com',
          my_reply: '无回复'
        },
      }
    },
    methods: {
      change() {
        this.modal_show = true
      }
    }
  }
</script>

