<style scoped lang="less">
  @import '../assets/my-style';

  .wrap {
    height: 100%;
    width: 100%;
    position: relative;
  }

  .wrap-div {
    width: 90%;
    position: relative;
    margin: 20px auto;
    height: 60px;
  }

  .title {
    width: 120px;
    height: 60px;
    position: relative;
    float: left;
    background-color: @white;
    > span {
      width: 100%;
      height: 100%;
      font-size: 24px;
    }
  }

  .title-input-div {
    width: 400px;
    height: 60px;
    position: relative;
    float: left;
  }

  .title-input {
    width: 100%;
    height: 100%;
    text-align: center;
    font-size: 24px;
    &:focus {
      box-shadow: 0 0 1px 2px @green;
    }
  }

  .editor-div {
    width: 90%;
    margin: auto;
    position: relative;
    margin-top: 50px;
  }

  .type {
    float: left;
    position: relative;
    width: 80px;
    height: 60px;
    > span {
      width: 100%;
      height: 100%;
    }
  }

  .span-left {
    margin-left: 20px;
  }
</style>

<template>
  <div class="wrap">
    <div class="wrap-div">
      <div class="title">
        <span class="flex-mid">标题:</span>
      </div>
      <div class="title-input-div">
        <input type="text" class="title-input" placeholder="请输入标题">
      </div>
    </div>
    <div class="wrap-div">
      <div class="type">
        <div class="btn2 flex-mid" @click="tranType">切换</div>
      </div>
      <div class="type"><span class="flex-mid font24 span-left">{{selectedType.text}}</span></div>
    </div>
    <div v-show="selectedType.type === 1" class="wrap-div">
      <div class="title">
        <span class="flex-mid">风格:</span>
      </div>
      <div class="title-input-div">
        <input type="text" class="title-input">
      </div>
    </div>
    <div class="editor-div">
      <div ref="editor" style="text-align: left"></div>
    </div>
    <div class="wrap-div flex-mid  right">
      <div class="btn2 flex-mid">发布</div>
    </div>
  </div>
</template>

<script>
  import E from 'wangeditor'

  export default {
    name: 'write',
    data() {
      return {
        contentType: [
          {type: 1, text: '日志'},
          {type: 2, text: '博文'},
          {type: 3, text: '说说'},
          {type: 4, text: '鸡汤'}
        ],
        selectedType: {type: 1, text: '日志'},
        editorContent: ''
      }
    },
    methods: {
      tranType() {
        this.selectedType = this.contentType[(this.selectedType.type) % 4]
      }
    },
    mounted() {
      const editor = new E(this.$refs.editor)
      editor.customConfig.onchange = (html) => {
        this.editorContent = html
      }
      editor.create()
    }
  }
</script>
