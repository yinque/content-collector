<script lang="ts" setup>

import YQLoader from "./YQLoader.vue";
import YQLoader2 from "./YQLoader2.vue";
import {onMounted} from "vue";
import {Loader} from "./index";

let loader: Loader;
onMounted(()=>{
  const l1 = document.querySelector("#l1")
  loader = new Loader(l1)
})
</script>

<template>
  <div class="yq-loader-test">
    <div class="container">
      <YQLoader size="30px"></YQLoader>
    </div>
    <div class="container">
      <YQLoader2 size="30px"></YQLoader2>
    </div>
    <div id="l1">

    </div>
    <button @click="loader.destroy()">销毁加载动画</button>
  </div>
</template>

<style scoped>
.container{
  width: 300px;
  height: 200px;
  border: 1px dashed green;
  position: relative;
}

#l1{
  width: 500px;
  height: 500px;
  border: 1px dashed green;
}

</style>

<script lang="ts">
export default {
  name: "YQLoaderTest"
}
</script>