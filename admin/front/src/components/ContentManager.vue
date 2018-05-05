<style scoped lang="less">
  @import "../assets/my-style";

  .table {
    width: 1370px;
    position: relative;
    margin: auto;
    margin-top: 40px;
  }

  .table-top {
    margin-top: 150px;
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
      width: 200px;
    }
    .span {
      text-overflow: ellipsis;
      overflow: hidden;
      word-break: keep-all;
      height: 100%;
      width: 100%;
      text-align: left;
    }
    .li-white {
      background-color: @white;
    }
  }

  .editor-style {
    position: relative;
    width: 100%;
    height: 100%;
  }

  .table-wrap {
    width: 100%;
    height: 100%;
  }
</style>

<template>
  <div class="wrap">
    <div class="table-wrap" v-show="!editor_show">
      <div class="table">
        <div class="table-header flex-mid left">
          <div class="table-header-text flex-mid"><span class="flex-mid">共3页 跳到</span></div>
          <div class="table-header-input"><input placeholder-style="color:white" type="text" class="input1"
                                                 placeholder="输入页数"></div>
          <div class="table-header-btn"><span class="flex-mid">确定跳转</span></div>
        </div>
        <ul class="ul">
          <li>
            <div class="flex-mid left">日 志</div>
            <div class="flex-mid left">标 题</div>
            <div class="flex-mid left">发布时间</div>
            <div class="flex-mid left">是否可见</div>
            <div class="flex-mid left">浏览数</div>
          </li>
          <li @click="editor(editor_type.log)">
            <div class="flex-mid left"><span class="span"></span></div>
            <div class="flex-mid left"><span class="span">结束不过开始</span></div>
            <div class="flex-mid left"><span class="span">2018-06-03 12:55:12</span></div>
            <div class="flex-mid left"><span class="span">是</span></div>
            <div class="flex-mid left"><span class="span">123</span></div>
          </li>
        </ul>
      </div>
      <div class="table table-top">
        <div class="table-header flex-mid left">
          <div class="table-header-text flex-mid"><span class="flex-mid">共3页 跳到</span></div>
          <div class="table-header-input"><input placeholder-style="color:white" type="text" class="input1"
                                                 placeholder="输入页数"></div>
          <div class="table-header-btn"><span class="flex-mid">确定跳转</span></div>
        </div>
        <ul class="ul">
          <li>
            <div class="flex-mid left">博 文</div>
            <div class="flex-mid left">标 题</div>
            <div class="flex-mid left">发布时间</div>
            <div class="flex-mid left">是否可见</div>
            <div class="flex-mid left">浏览数</div>
          </li>
          <li @click="editor(editor_type.blog)">
            <div class="flex-mid left"><span class="span"></span></div>
            <div class="flex-mid left"><span class="span">结束不过开始</span></div>
            <div class="flex-mid left"><span class="span">2018-06-03 12:55:12</span></div>
            <div class="flex-mid left"><span class="span">是</span></div>
            <div class="flex-mid left"><span class="span">123</span></div>
          </li>
        </ul>
      </div>
      <div class="table table-top">
        <div class="table-header flex-mid left">
          <div class="table-header-text flex-mid"><span class="flex-mid">共3页 跳到</span></div>
          <div class="table-header-input"><input placeholder-style="color:white" type="text" class="input1"
                                                 placeholder="输入页数"></div>
          <div class="table-header-btn"><span class="flex-mid">确定跳转</span></div>
        </div>
        <ul class="ul">
          <li>
            <div class="flex-mid left">说 说</div>
            <div class="flex-mid left">标 题</div>
            <div class="flex-mid left">发布时间</div>
            <div class="flex-mid left">是否可见</div>
            <div class="flex-mid left">点赞数</div>
          </li>
          <li @click="editor(editor_type.saySomething)">
            <div class="flex-mid left"><span class="span"></span></div>
            <div class="flex-mid left"><span class="span">结束不过开始</span></div>
            <div class="flex-mid left"><span class="span">2018-06-03 12:55:12</span></div>
            <div class="flex-mid left"><span class="span">是</span></div>
            <div class="flex-mid left"><span class="span">123</span></div>
          </li>
        </ul>
      </div>
      <div class="table table-top">
        <div class="table-header flex-mid left">
          <div class="table-header-text flex-mid"><span class="flex-mid">共3页 跳到</span></div>
          <div class="table-header-input"><input placeholder-style="color:white" type="text" class="input1"
                                                 placeholder="输入页数"></div>
          <div class="table-header-btn"><span class="flex-mid">确定跳转</span></div>
        </div>
        <ul class="ul">
          <li>
            <div class="flex-mid left">鸡 汤</div>
            <div class="flex-mid left">标 题</div>
            <div class="flex-mid left">发布时间</div>
            <div class="flex-mid left">是否可见</div>
            <div class="flex-mid left">浏览数</div>
          </li>
          <li @click="editor(editor_type.motto)">
            <div class="flex-mid left"><span class="span"></span></div>
            <div class="flex-mid left"><span class="span">结束不过开始</span></div>
            <div class="flex-mid left"><span class="span">2018-06-03 12:55:12</span></div>
            <div class="flex-mid left"><span class="span">是</span></div>
            <div class="flex-mid left"><span class="span">123</span></div>
          </li>
        </ul>
      </div>
    </div>
    <editor-component v-show="editor_show" ref="edco" @close="editor_show = false"
                      class="editor-style"></editor-component>
  </div>
</template>

<script>
  import EditorComponent from './EditorComponent'
  import {editor_type, editor_status} from "../constant";

  export default {
    name: 'contentManager',
    components: {EditorComponent},
    data() {
      return {
        editor_type: editor_type,
        editor_show: false
      }
    },
    methods: {
      editor(type) {
        const editor = this.$refs["edco"]
        editor.setData(editor_status.update)
        this.editor_show = true
      }
    }
  }
</script>

