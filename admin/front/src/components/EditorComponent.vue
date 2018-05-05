<style scoped lang="less">
  @import '../assets/my-style';

  .wrap {
    overflow: hidden;
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

  .close-div {
    width: 120px;
    height: 100%;
    position: relative;
    float: right;
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
      <div class="close-div" v-show="component_status === editor_status.update">
        <div class="btn2 flex-mid" @click="close()">关闭</div>
      </div>
    </div>
    <div class="wrap-div">
      <div class="type">
        <div class="btn2 flex-mid" @click="tranType">切换</div>
      </div>
      <div class="type"><span class="flex-mid font24 span-left">{{selected_type.text}}</span></div>
    </div>
    <div v-show="selected_type.type === editor_type.log" class="wrap-div">
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
    <div v-if="component_status === editor_status.insert" class="wrap-div flex-mid  right">
      <div class="btn2 flex-mid">发布</div>
    </div>
    <div v-else class="wrap-div flex-mid  right">
      <div class="btn2 flex-mid">更新</div>
    </div>
  </div>
</template>

<script>
  import E from 'wangeditor'
  import { editor_status, editor_type } from "../constant";
  export default {
    name: 'write',
    data() {
      return {
        editor_status: editor_status,
        editor_type: editor_type,
        component_status: editor_status.update,
        content_type: [
          {type: editor_type.log, text: '日志'},
          {type: editor_type.blog, text: '博文'},
          {type: editor_type.saySomething, text: '说说'},
          {type: editor_type.motto, text: '鸡汤'}
        ],
        selected_type: {type: editor_type.log, text: '日志'},
        editor_content: '',
        data: null
      }
    },
    methods: {
      // 外部传值进来
      setData (data) {
        this.component_status = data
        // this.selected_type = this.content_type.filter(item => { item.type === data })[0]
      },
      // 关闭
      close () {
        this.$emit('close')
      },
      tranType() {
        this.selectedType = this.contentType[(this.selectedType.type) % 4]
      }
    },
    mounted() {
      const editor = new E(this.$refs.editor)
      editor.customConfig.onchange = (html) => {
        this.editor_content = html
      }
      editor.create()
    }
  }
</script>
