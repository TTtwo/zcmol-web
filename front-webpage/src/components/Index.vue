<style scoped lang="less">
  @import "../assets/my-style";

  #index {
    width: 100%;
    height: 100%;
    background: url("../assets/bg.gif") repeat;
    .header {
      height: 25%;
      position: relative;
      .logo-wrapper {
        width: 30%;
        height: 100%;
        .flex(@h: flex-start);

        .logo {
          width: 100%;
          height: 100%;
          max-height: 196px;
          max-width: 256px;
          background: url("../assets/logo.png") no-repeat center;
          background-size: contain;
        }
      }
    }
    .container {
      position: relative;
      width: 100%;
      height: 75%;
      overflow: hidden;
      .content-wrapper {
        width: 100%;
        height: 500%;
        .content-page {
          height: 20%;
          width: 100%;
        }
      }
    }
    @media (max-width: 1024px) {
      .header {
        height: 20%;
      }

      .container {
        height: 80%;
      }
    }
  }
</style>

<template>
  <div id="index">
    <div class="header">
      <div class="logo-wrapper">
        <div class="logo"></div>
      </div>
    </div>
    <div class="container">
      <div class="content-wrapper">
        <!--<daily-comp class="content-page"></daily-comp>-->
        <!--<guestbook-comp class="content-page"></guestbook-comp>-->
        <link-comp class="content-page"></link-comp>
      </div>
    </div>
  </div>
</template>

<script>
  import DailyComp from './common/DailyComponent'
  import GuestbookComp from './common/GuestbookComponent'
  import LinkComp from './common/LinkComponent'

  export default {
    name: 'index',
    components: {DailyComp, GuestbookComp, LinkComp}
  }
</script>
