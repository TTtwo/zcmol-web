<style scoped lang="less">
  @import "../../assets/my-style";

  #pag {
    height: 80px;
    position: relative;
    .flex(@horizontal: flex-end);
    .font-style(22px; @green);

    .page-text {
      height: 60px;
      margin: 20px 0;
      padding: 0 10px;
      position: relative;
      background-color: @green-white;
      .flex();
    }

    .page-input {
      float: left;
      width: 120px;
      height: 60px;
      position: relative;

      input {
        .base-input(@bsc: @green);

        &::-moz-placeholder,
        &::-webkit-input-placeholder {
          color: lighten(@black-blue, 10);
          text-align: center;
        }
      }
    }

    .page-btn {
      .flex();
      .base-btn(@bgc: @green-white);
    }
  }
</style>

<template>
  <div id="pag">
    <div class="page-text"><span>共3页 跳到</span></div>
    <div class="page-input"><input placeholder-style="color:white" type="text" class="input1"
                                   placeholder="输入页数"></div>
    <div class="page-btn"><span>确定跳转</span></div>
    <div class="page-btn"><span>上一页</span></div>
    <div class="page-btn"><span>下一页</span></div>
  </div>
</template>

<script>
  export default {
    name: 'paging'
  }
</script>
