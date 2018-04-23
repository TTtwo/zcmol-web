<style scoped lang="less">
  @import '../assets/my-style';
  .wrap {
    width: 100%;
    height: 100%;
  }
</style>

<template>
  <div class="wrap">
    <editor-component ref="edco">
    </editor-component>
  </div>
</template>

<script>
  import EditorComponent from './EditorComponent'
  import { editor_status } from "../constant";

  export default {
    name: 'write',
    components: { EditorComponent },
    data () {
      return {
      }
    },
    mounted() {
      const editor = this.$refs["edco"]
      editor.setData(editor_status.insert)
    }
  }
</script>
