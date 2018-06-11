<style scoped lang="less">
  @import "../../assets/my-style";

  #comment-component {
    width: 100%;
    height: 100%;
    overflow-x: hidden;
    overflow-y: scroll;

    .content-wrapper {
      margin: 20px 60px;

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
            width: 80px;
            height: 80px;
            border-radius: 10px;
            border: 1px solid @comment_bg;
            overflow: hidden;
            box-shadow: 0 0 5px @comment_bg;
            transition: border-radius .5s ease-in-out;
            float: left;
            img {
              width: 80px;
              height: 80px;
            }
            &:hover {
              border-radius: 80px;
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
                height: 50%;
                .flex(@h: flex-start);
              }
              a {
                font-size: 24px;
                display: block;
                height: 50%;
                color: white;
                .flex(@h: flex-start;@v: flex-end);
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
            margin: 100px 0 40px 0;
            text-indent: 2em;
            padding-left: 80px;
            font-size: 24px;
            line-height: 36px;
            color: @comment_bg;
          }
        }
      }
      .ul-lv2 {
        padding-left: 80px;
      }
    }
    .write-wrapper {
      position: absolute;
      width: 100%;
      bottom: 0;

      .write-container {
        height: 80px;
        width: 100%;
        background-color: @barColor;

        .write {
          height: 80px;
          width: 50%;
          position: relative;
          float: left;

          .icon {
            width: 80px;
            height: 80px;
            background-color: #373737;
            .flex;
            img {
              width: 60px;
              height: 60px;
            }
          }
          input {
            display: block;
            position: absolute;
            left: 80px;
            top: 0;
            height: 80px;
            width: calc(100% - 80px);
            outline: none;
            background-color: @barColor;
            color: @comment_bg;
            border: none;
            font-size: 24px;
            font-family: zcmol;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            padding: 0 20px;
          }
        }
      }
      .w-anim {
        -webkit-transition: margin-left .6s;
        -moz-transition: margin-left .6s;
        -ms-transition: margin-left .6s;
        -o-transition: margin-left .6s;
        transition: margin-left .6s;
        transition-timing-function: ease-in-out;
      }
      .left-animation-start {
        margin-left: -100%;
        .w-anim;
      }
      .right-animation-start {
        margin-left: 100%;
        .w-anim;
      }
      .left-animation-end {
        margin-left: 0;
      }
    }

    .write-btn {
      .circle-btn;
      position: absolute;
      right: 12px;
      top: 90px;
    }
  }
</style>

<template>
  <div id="comment-component">
    <div class="content-wrapper">
      <ul class="ul-lv1">
        <li class="ul-lv1-li">
          <div class="avatar">
            <img src="../../assets/logo.png">
          </div>
          <div class="info-wrapper">
            <div class="info">
              <a href="http://zcmol.cn" target="_blank">早茶月光</a>
              <span>Time: 2016:03:06 23:54:46</span>
            </div>
            <aside class="aside">
              <div class="comment">
                <img src="../../assets/comment.png">
              </div>
            </aside>
          </div>
          <div class="content">
            <p>北极星的眼泪
            </p>
          </div>
          <ul class="ul-lv1 ul-lv2">
            <li class="ul-lv1-li">
              <div class="avatar">
                <img src="../../assets/logo.png">
              </div>
              <div class="info-wrapper">
                <div class="info">
                  <a href="http://zcmol.cn" target="_blank">早茶月光</a>
                  <span>Time: 2016:03:06 23:54:46</span>
                </div>
                <aside class="aside">
                  <div class="comment">
                    <img src="../../assets/comment.png">
                  </div>
                </aside>
              </div>
              <div class="content">
                <p>北极星的眼泪
                </p>
              </div>
              <ul class="ul-lv1 ul-lv2">
                <li class="ul-lv1-li">
                  <div class="avatar">
                    <img src="../../assets/logo.png">
                  </div>
                  <div class="info-wrapper">
                    <div class="info">
                      <a href="http://zcmol.cn" target="_blank">早茶月光</a>
                      <span>Time: 2016:03:06 23:54:46</span>
                    </div>
                    <aside class="aside">
                      <div class="comment">
                        <img src="../../assets/comment.png">
                      </div>
                    </aside>
                  </div>
                  <div class="content">
                    <p>北极星的眼泪
                    </p>
                  </div>
                  <ul class="ul-lv1 ul-lv2">
                    <li class="ul-lv1-li">
                      <div class="avatar">
                        <img src="../../assets/logo.png">
                      </div>
                      <div class="info-wrapper">
                        <div class="info">
                          <a href="http://zcmol.cn" target="_blank">早茶月光</a>
                          <span>Time: 2016:03:06 23:54:46</span>
                        </div>
                        <aside class="aside">
                          <div class="comment">
                            <img src="../../assets/comment.png">
                          </div>
                        </aside>
                      </div>
                      <div class="content">
                        <p>北极星的眼泪
                        </p>
                      </div>
                      <ul class="ul-lv1 ul-lv2">
                        <li class="ul-lv1-li">
                          <div class="avatar">
                            <img src="../../assets/logo.png">
                          </div>
                          <div class="info-wrapper">
                            <div class="info">
                              <a href="http://zcmol.cn" target="_blank">早茶月光</a>
                              <span>Time: 2016:03:06 23:54:46</span>
                            </div>
                            <aside class="aside">
                              <div class="comment">
                                <img src="../../assets/comment.png">
                              </div>
                            </aside>
                          </div>
                          <div class="content">
                            <p>北极星的眼泪
                            </p>
                          </div>
                          <ul class="ul-lv1 ul-lv2">
                            <li class="ul-lv1-li">
                              <div class="avatar">
                                <img src="../../assets/logo.png">
                              </div>
                              <div class="info-wrapper">
                                <div class="info">
                                  <a href="http://zcmol.cn" target="_blank">早茶月光</a>
                                  <span>Time: 2016:03:06 23:54:46</span>
                                </div>
                                <aside class="aside">
                                  <div class="comment">
                                    <img src="../../assets/comment.png">
                                  </div>
                                </aside>
                              </div>
                              <div class="content">
                                <p>北极星的眼泪
                                </p>
                              </div>
                              <ul class="ul-lv1 ul-lv2">
                                <li class="ul-lv1-li">
                                  <div class="avatar">
                                    <img src="../../assets/logo.png">
                                  </div>
                                  <div class="info-wrapper">
                                    <div class="info">
                                      <a href="http://zcmol.cn" target="_blank">早茶月光</a>
                                      <span>Time: 2016:03:06 23:54:46</span>
                                    </div>
                                    <aside class="aside">
                                      <div class="comment">
                                        <img src="../../assets/comment.png">
                                      </div>
                                    </aside>
                                  </div>
                                  <div class="content">
                                    <p>北极星的眼泪
                                    </p>
                                  </div>
                                  <ul class="ul-lv1 ul-lv2">
                                    <li class="ul-lv1-li">
                                      <div class="avatar">
                                        <img src="../../assets/logo.png">
                                      </div>
                                      <div class="info-wrapper">
                                        <div class="info">
                                          <a href="http://zcmol.cn" target="_blank">早茶月光</a>
                                          <span>Time: 2016:03:06 23:54:46</span>
                                        </div>
                                        <aside class="aside">
                                          <div class="comment">
                                            <img src="../../assets/comment.png">
                                          </div>
                                        </aside>
                                      </div>
                                      <div class="content">
                                        <p>北极星的眼泪
                                        </p>
                                      </div>
                                      <ul class="ul-lv1 ul-lv2">
                                        <li class="ul-lv1-li">
                                          <div class="avatar">
                                            <img src="../../assets/logo.png">
                                          </div>
                                          <div class="info-wrapper">
                                            <div class="info">
                                              <a href="http://zcmol.cn" target="_blank">早茶月光</a>
                                              <span>Time: 2016:03:06 23:54:46</span>
                                            </div>
                                            <aside class="aside">
                                              <div class="comment">
                                                <img src="../../assets/comment.png">
                                              </div>
                                            </aside>
                                          </div>
                                          <div class="content">
                                            <p>北极星的眼泪
                                            </p>
                                          </div>
                                          <ul class="ul-lv1 ul-lv2">
                                            <li class="ul-lv1-li">
                                              <div class="avatar">
                                                <img src="../../assets/logo.png">
                                              </div>
                                              <div class="info-wrapper">
                                                <div class="info">
                                                  <a href="http://zcmol.cn" target="_blank">早茶月光</a>
                                                  <span>Time: 2016:03:06 23:54:46</span>
                                                </div>
                                                <aside class="aside">
                                                  <div class="comment">
                                                    <img src="../../assets/comment.png">
                                                  </div>
                                                </aside>
                                              </div>
                                              <div class="content">
                                                <p>北极星的眼泪
                                                </p>
                                              </div>
                                            </li>
                                          </ul>
                                        </li>
                                      </ul>
                                    </li>
                                  </ul>
                                </li>
                              </ul>
                            </li>
                          </ul>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </li>
              </ul>
            </li>
          </ul>
        </li>
        <li class="ul-lv1-li">
          <div class="avatar">
            <img src="../../assets/logo.png">
          </div>
          <div class="info-wrapper">
            <div class="info">
              <a href="http://zcmol.cn" target="_blank">早茶月光</a>
              <span>Time: 2016:03:06 23:54:46</span>
            </div>
            <aside class="aside">
              <div class="comment">
                <img src="../../assets/comment.png">
              </div>
            </aside>
          </div>
          <div class="content">
            <p>asdfasdf asdfasdf hsadfh lkasdjflk asdfj
            </p>
          </div>
        </li>
      </ul>
    </div>
    <div class="write-wrapper">
      <div class="write-container left-animation-start" :class="{'left-animation-end': is_write}">
        <div class="write">
          <div class="icon"><img src="../../assets/me1.png"></div>
          <input type="text" placeholder="Email">
        </div>
        <div class="write">
          <div class="icon"><img src="../../assets/messagebook1.png"></div>
          <input type="text" placeholder="Web site">
        </div>
      </div>
      <div class="write-container right-animation-start" :class="{'left-animation-end': is_write}">
        <div class="write">
          <div class="icon"><img src="../../assets/me1.png"></div>
          <input type="text" placeholder="Nick name">
        </div>
        <div class="write">
          <div class="icon"><img src="../../assets/messagebook1.png"></div>
          <input type="text" placeholder="content">
        </div>
      </div>
    </div>
    <div class="write-btn" @click="is_write = !is_write">W</div>
  </div>
</template>

<script>
  export default {
    name: 'comment-component',
    data() {
      return {
        is_write: false,
      }
    }
  }
</script>
