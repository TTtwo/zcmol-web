<style scoped lang="less">
  @import "../assets/my-style";
  .wrap{
    width: 100%;
    height: 100%;
  }
  .table {
    width: 90%;
    margin-left: 5%;
    margin-top: 40px;
  }
  .ul {
    width: 100%;
    > li {
      width: 100%;
      height: 70px;
      position: relative;
      font-size: 22px;
    }
    > li:first-child {
      background-color: @green;
      color: @white;
    }
    > li > div {
      position: relative;
      float: left;
      height: 70px;
      line-height: 70px;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
      word-break: keep-all;
    }
    .name {
      margin-left: 20px;
      width: 160px;
    }
    .content {
      margin-left: 20px;
      width: 300px;
    }
  }

</style>

<template>
  <div class="wrap">
    <div class="table">
      <ul class="ul">
        <li>
          <div class="name flex-mid left">昵  称</div>
          <div class="content flex-mid left">内  容</div>
          <div></div>
          <div></div>
          <div></div>
        </li>
        <li>
          <div class="name flex-mid left">我是小老拉时代峻峰拉水电费</div>
          <div class="content flex-mid left">阿大山里的开发撒的浪费捡垃圾水电费炼金啊说的福利看手机对</div>
          <div></div>
          <div></div>
          <div></div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'guestbook',

  }
</script>
