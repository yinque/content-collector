<script setup>
// 右键菜单组件测试
import {showContextMenu} from "./index";

const menuItems = [
    {
        name: "删除", method: () => {
            console.log("删除")
        }
    },
    {
        name: "修改", method: () => {
            console.log("修改")
        }
    },
    {
        name: "查询", method: () => {
            console.log("查询")
        }
    },
]
// 处理右键 事件函数
function handleRC(event){
  showContextMenu(event,menuItems)
}
</script>

<template>
  <div class="menu-test">
    MenuTest
    <div class="yellow block big" @click.right="handleRC">
    </div>
  </div>
</template>

<style scoped>
/*调试用*/
.block{
  display: block;
  width: 50px;
  height: 50px;
}
.big{
  width: 800px;
  height: 800px;
}
.red{
  background-color: red;
}
.green{
  background-color: green;
}
.yellow {
  background-color: rgb(255, 213, 59);
}
</style>


<script>
export default {
  name: "YQContextMenuTest"
}
</script>