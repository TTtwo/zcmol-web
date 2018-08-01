<style lang="less">
  @import "../../assets/my-style";

  .ul-lv1 {
    list-style: none;
    overflow-x: scroll;
    .ul-lv1-li {
      width: 100%;
      text-align: left;
      position: relative;
      padding: 1px;
      margin-top: 2px;
      &::after {
        content: '';
        display: block;
        visibility: hidden;
        height: 0;
        clear: both;
      }
      .avatar {
        width: 70px;
        height: 70px;
        overflow: hidden;
        box-shadow: 0 0 5px @comment_bg;
        transition: border-radius .5s ease-in-out;
        float: left;

        img {
          width: 70px;
          height: 70px;
        }

      }
      .info-wrapper {
        float: left;
        margin-left: 10px;
        height: 80px;
        color: @comment_bg;
        font-size: 20px;
        font-family: beleren;

        .info {
          height: 80px;
          position: relative;
          float: left;

          span {
            display: block;
            color: #999;
            height: 50%;
            .flex(@h: flex-start);
          }

          a {
            font-size: 24px;
            display: block;
            height: 50%;
            color: #bababa;
            .flex(@h: flex-start; @v: flex-start);

            &:hover {
              color: @green;
            }

          }
        }
        .aside {
          height: 80px;
          width: 80px;
          position: relative;
          float: left;
          display: none;

          .comment {
            height: 50px;
            width: 50px;
            background-color: @barColor;
            -webkit-border-radius: 50px;
            -moz-border-radius: 50px;
            border-radius: 50px;
            .flex;

            img {
              width: 25px;
              height: 25px;

              &:hover {
                opacity: .6;
                cursor: pointer;
              }

            }
          }
        }
        &:hover .aside {
          .flex;
        }

      }
      .content {
        position: relative;
        margin: 80px 0 20px 0;
        text-indent: 2em;
        padding-left: 80px;
        font-size: 24px;
        line-height: 36px;
        color: #ff9ca9;
      }
    }
  }

  .ul-lv2 {
    padding-left: 80px;
  }
</style>
<template>
  <div>
    <ul class="ul-lv1 ul-lv2" v-for="item, index in comments">
      <li class="ul-lv1-li">
        <div class="avatar">
          <img :src="getAvatar(item.email, false)">
        </div>
        <div class="info-wrapper">
          <div class="info">
            <a href="http://zcmol.cn" target="_blank">{{item.nickname}}</a>
            <span>Time: {{timeTransform(item.create_at)}}</span>
          </div>
          <aside class="aside">
            <div class="comment">
              <img @click="emitId(item.id)" src="../../assets/comment.png">
            </div>
          </aside>
        </div>
        <div class="content">
          <p>-- {{item.content}}
          </p>
        </div>
        <sub-comment :comments="item.subComments" :id="id" @replyId="emitId"></sub-comment>
      </li>
    </ul>
  </div>
</template>
<script>
  import subComment from './subCommentComponent'
  import {timeTransform, getAvatar} from "../../util";

  export default {
    name: 'subComment',
    components: {subComment},
    props: ['comments', 'id'],
    methods: {
      timeTransform: timeTransform,
      getAvatar: getAvatar,
      emitId(id) {
        this.$emit('replyId', id)
      }
    },
    watch: {
      id: function (id) {
        this.id = id
      }
    }
  }
</script>
