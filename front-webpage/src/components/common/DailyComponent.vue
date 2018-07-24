<style scoped lang="less">
  @import "../../assets/my-style";

  ::-webkit-scrollbar {
    display: none;
  }

  #daily {
    overflow: hidden;
    ul {
      width: 100%;
      height: 100%;
      list-style: none;
      li {
        width: 20%;
        height: 33.3%;
        float: left;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
        border: 2px solid #333;
        font-family: 'impact', arial;
        .flex(@h: none);
        overflow: hidden;
        .home-div {
          position: relative;
          width: 100%;
          height: 100%;
          .wp {
            position: relative;
            left: -100%;
            width: 200%;
            height: 100%;
            transition: left .2s ease-in-out;
            .hdiv1, .hdiv2 {
              width: 50%;
              height: 100%;
              float: left;
              .flex(@h: none);
              .dp {
                width: 100%;
                > span {
                  width: 100%;
                  display: block;
                  .flex(@h: flex-end);
                  padding-right: 20px;
                  -webkit-box-sizing: border-box;
                  -moz-box-sizing: border-box;
                  box-sizing: border-box;
                }
                .day {
                  font-size: 80px;
                }
                .info {
                  font-size: 20px;
                  font-family: motto;
                }
                .title {
                  font-size: 24px;
                }
              }
            }
            .hdiv1 {
              background-color: @green;
              .day {
                color: #222;
              }
              .info {
                color: #3d3d3d;
              }
            }
            .hdiv2 {
              color: #777;
            }
            &:hover {
              left: 0;
              cursor: pointer;
            }
          }
        }
      }
      li:first-child {
        background-color: @green;
        border-width: 1px;
        .daily-div {
          width: 100%;
          > span {
            width: 100%;
            display: block;
            .flex(@h: flex-end);
            padding-right: 20px;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
          }
          .day {
            font-size: 80px;
            color: #222;
          }
          .info {
            color: #3d3d3d;
            font-size: 24px;
            font-family: beleren;
          }
        }
      }
      li:nth-child(2) {
        background: url("../../assets/two.png") no-repeat center;
        background-size: cover;
        border-width: 1px;
      }
      @media (max-width: 1024px) {
        li {
          height: 25%;
          width: 50%;
        }
      }
    }
  }

  @media (max-width: 1024px) {
    #daily {
      overflow-y: scroll;
    }
  }
</style>
<template>
  <div id="daily">
    <ul>
      <li>
        <div class="daily-div">
          <span class="day">11</span>
          <span class="info">2016.09</span>
          <span class="info">The truth that you leave</span>
          <span class="info">Log+</span>
        </div>
      </li>
      <li></li>
      <li v-for="item, index in daily_array">
        <div class="home-div">
          <a @click="toDaily(item.article.id)">
            <div class="wp">
              <div class="hdiv1">
                <div class="dp">
                  <span class="day">{{getYM_D(item.article.create_at, 0)}}</span>
                  <span class="info">{{getYM_D(item.article.create_at)}}</span>
                  <span class="info title">{{item.title}}</span>
                  <span class="info">{{item.daily_type}}</span>
                </div>
              </div>
              <div class="hdiv2">
                <div class="dp">
                  <span class="day">{{getYM_D(item.article.create_at, 0)}}</span>
                  <span class="info">{{getYM_D(item.article.create_at)}}</span>
                  <span class="info title">{{item.title}}</span>
                  <span class="info">{{item.daily_type}}</span>
                </div>
              </div>
            </div>
          </a>
        </div>
      </li>
    </ul>
  </div>
</template>
<script>
  export default {
    name: 'daily',
    props: ['daily'],
    data() {
      return {
        daily_array: this.daily,
      }
    },
    methods: {
      getYM_D(time, YM = true) {
        const date = new Date(time * 1000)
        const timeAry = date.toLocaleDateString().split('/')
        return YM
          ? timeAry[0] + "." + timeAry[1]
          : timeAry[2].length < 2
            ? '0' + timeAry[2]
            : timeAry[2]
      },
      toDaily(id){
        this.$router.push({
          name: 'daily_article',
          params: {
            article_id: id
          }
        })
      }
    },
    watch: {
      daily: function (daily) {
        this.daily_array = daily
      }
    }
  }
</script>

