<style scoped lang="less">
  @import "../../assets/my-style";
  #pag {
    height: 80px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    font-size: 22px;
  }
  .page-text{
    padding: 0 10px;
    height: 60px;
    position: relative;
    margin: 20px 0;
    background-color: @white;
    span {
      height: 100%;
      position: relative;
      margin: 0 15px;
    }
  }

  .page-input {
    position: relative;
    float: left;
    width: 120px;
    height: 60px;
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

  .page-btn {
    height: 60px;
    position: relative;
    float: left;
    background-color: @white;
    padding: 0 10px;
    &:hover {
      background-color: @green-white;
      cursor: pointer;
    }
    &:active {
      border: 1px solid @green-white;
    }
  }

</style>

<template>
  <div id="pag">
    <div class="page-text flex-mid"><span class="flex-mid">共3页 跳到</span></div>
    <div class="page-input"><input placeholder-style="color:white" type="text" class="input1"
                                           placeholder="输入页数"></div>
    <div class="page-btn flex-mid marRih10"><span class="flex-mid">确定跳转</span></div>
    <div class="page-btn flex-mid"><span class="flex-mid">上一页</span></div>
    <div class="page-btn flex-mid"><span class="flex-mid">下一页</span></div>
  </div>
</template>

<script>
  export default {
    name: 'paging'
  }
</script>
