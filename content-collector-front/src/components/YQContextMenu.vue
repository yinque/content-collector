<script setup lang="ts">
/*
其中有两个元素：监察守卫与右键菜单。
监察守卫定义父元素的右键菜单事件
 */
import {defineProps, onMounted, ref} from "vue";


const props = defineProps({
  contextItem: {
    type: Array,
    default: () => []
  }
});
// 获取 DOM 元素
// const myElement = document.getElementById('myElement');
const markRef =ref()
const contextMenuRef = ref();

// console.log(props.targetElement)
// 定义右键事件处理函数
function handleContextMenu(event) {
  event.preventDefault(); // 阻止默认右键菜单

  // 设置上下文菜单的位置
  contextMenuRef.value.style.left = `${event.clientX}px`;
  contextMenuRef.value.style.top = `${event.clientY}px`;

  // 显示上下文菜单
  contextMenuRef.value.style.display = 'block';
}

onMounted(()=>{
  // 绑定右键事件监听器
  markRef.value.parentNode.addEventListener('contextmenu', handleContextMenu);

  // 点击页面其他地方时隐藏上下文菜单
    document.addEventListener('click', function(event) {
      // todo
      contextMenuRef.value.style.display = 'none';
  });
})

</script>
<template>
  <div class="hidden-el" ref="markRef"></div>
  <ul class="context-menu" ref="contextMenuRef">
    <li v-for="i of props.contextItem" @click="i.handler">{{i.name}}</li>
  </ul>
</template>

<script lang="ts">
export default {
  name: "YQContextMenu"
}
</script>

<style scoped>
.hidden-el{
  display: none;
}
.context-menu {
  position: absolute;
  display: none;
  list-style: none;
  padding: 0;
  margin: 0;
  background-color: white;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
.context-menu li {
  padding: 8px 16px;
  cursor: pointer;
}
</style>