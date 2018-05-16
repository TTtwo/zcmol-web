<style scoped lang="less">
  @import "../assets/my-style";

  .mod {
    .table,
    .page-component {
      width: 1370px;
      margin: 40px auto auto auto;
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
  }

  .modal {

    .modal-btn-wrapper {
      width: 100%;
      height: 80px;
      margin-top: 30px;
      position: relative;
      .flex(@horizontal: flex-end);

      .modal-input-item {
        width: 220px;
        height: 60px;
        position: relative;
        margin-right: 20px;
        .flex();

        input {
          .font-style(28px; @black);
          .base-input(@bsc: @green);
        }
      }

      .btn {
        margin-left: 5px;
        border-radius: 5px;
        .base-btn(@bgc: @green-white);
        .font-style(24px; @black);
        .flex();

        &:hover {
          color: @white;
        }
      }
    }
  }
</style>

<template>
  <div class="mod">
    <div class="table">
      <div class="table-title">
        <div class="article">日 志</div>
        <div class="name">昵 称</div>
        <div class="time">时 间</div>
        <div class="content">内 容</div>
        <div class="email">邮 箱</div>
      </div>
      <ul class="table-ul">
        <li @click="change">
          <div class="article"><span>结束不过开始</span></div>
          <div class="name"><span>我是小老拉时代峻峰拉水电费</span></div>
          <div class="time"><span>2018-06-03 12:55:12</span></div>
          <div class="content"><span>阿大山里的开发撒的浪费捡垃圾水电费炼金啊说的福利看手机对</span></div>
          <div class="email"><span>1297075993@qq.com</span></div>
        </li>
      </ul>
    </div>
    <page-comp class="page-component"></page-comp>
    <Modal v-model="modal_show" class="modal">
      <div class="modal-item" v-for="(item, key) in modal_data" :key="key">
        <div class="modal-title"><span> {{ modalKeyText[key] }}</span></div>
        <div class="modal-content"><span>{{ item }}</span></div>
      </div>
      <div class="modal-item">
        <textarea class="modal-textarea" placeholder="输入/修改 我的回复"></textarea>
      </div>
      <div class="modal-btn-wrapper">
        <div class="modal-input-item">
          <input type="text"placeholder="删除/修改/回复"/>
        </div>
        <div class="btn">
          删除
        </div>
        <div class="btn">
          修改
        </div>
      </div>
    </Modal>
  </div>
</template>

<script>
  import PageComp from './common/PagingComponent'
  import {MODALKEYTEXT} from "../constant";

  export default {
    name: 'articleComment',
    components: {PageComp},
    data() {
      return {
        modalKeyText: MODALKEYTEXT,
        modal_show: false,
        modal_data: {
          id: '1',
          nickName: 'safas',
          website: '',
          target_nickName: '回复的人名',
          target_content: '回复的人的内容',
          reply_content: '回复内容'
        }
      }
    },
    methods: {
      change() {
        this.modal_show = true
      }
    }
  }
</script>



















