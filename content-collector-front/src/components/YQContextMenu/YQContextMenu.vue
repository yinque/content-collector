<script setup lang="ts">

interface MenuItem{
  name: string;
  method: Function;
}
const props = defineProps({
  menuItems: Array as () => MenuItem[]
});

// 移除自身
function remove(){
  const element = document.querySelector('.yq-context-menu')
  const removeEvent = new CustomEvent('remove', { detail: 'remove menu',bubbles:true });
  element.dispatchEvent(removeEvent)
}
</script>
<template>
  <div class="yq-context-menu"
       @click.right="e=>e.preventDefault()"
  >
    <ul @click="remove">
      <li v-for="m of props.menuItems" @click="m.method">{{m.name}}</li>
    </ul>
  </div>
</template>

<style lang="scss" scoped>
  .yq-context-menu{
    box-shadow: 0 1px 2px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.07), 0 4px 8px rgba(0,0,0,0.07), 0 8px 16px rgba(0,0,0,0.07), 0 16px 32px rgba(0,0,0,0.07), 0 32px 64px rgba(0,0,0,0.07);
  }
  ul{
    min-height: 1em;
    min-width: 3em;
    background-color: #f0f0f0;
  }
  //常用菜单样式
  ul {
    list-style-type: none; /* 移除列表默认的项目符号 */
    margin: 0;
    padding: 0;
  }

  li {
    padding: 8px 12px; /* 添加一些内边距，增加点击区域 */
    cursor: pointer; /* 设置光标样式为指针，表示可点击 */
    background-color: #f0f0f0; /* 背景色 */
    border-bottom: 1px solid #ccc; /* 底部边框分隔线 */
  }

  li:hover {
    background-color: #ddd; /* 鼠标悬停时的背景色 */
  }

  li:last-child {
    border-bottom: none; /* 最后一个列表项去除底部边框分隔线 */
  }
</style>
