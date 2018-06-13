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
                  font-size: 24px;
                  font-family: beleren;
                }
              }
            }
            .hdiv1 {
              background-color: @green;
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
          <span class="info">Forget</span>
          <span class="info">Log+</span>
        </div>
      </li>
      <li></li>
      <li>
        <div class="home-div">
          <a href="http://zcmol.cn">
            <div class="wp">
              <div class="hdiv1">
                <div class="dp">
                  <span class="day">17</span>
                  <span class="info">2018.04</span>
                  <span class="info">你好</span>
                  <span class="info">Log+</span>
                </div>
              </div>
              <div class="hdiv2">
                <div class="dp">
                  <span class="day">17</span>
                  <span class="info">2018.04</span>
                  <span class="info">你好</span>
                  <span class="info">Log+</span>
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
    name: 'daiyl',
  }
</script>

