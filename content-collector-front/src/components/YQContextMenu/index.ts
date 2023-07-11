/*
右键菜单组件
 */
import YQContextMenu from './YQContextMenu.vue'
import {createApp, h} from "vue";

export function showContextMenu(event, menuItems = []) {
    // body创建app容器
    const root = document.createElement('div')
    document.body.appendChild(root)

    // 获取指针位置
    const [x, y] = [event.pageX, event.pageY];
    // 设置root位置
    root.style.position = "absolute";
    root.style.left = x + "px";
    root.style.top = y + "px";
    // 创建app
    const app = createApp(() => h(YQContextMenu, {
        menuItems
    }))
    // 渲染组件到root元素上
    app.mount(root)

    // 移除弹窗方法
    const removeRoot = () => {
        app.unmount()
        root.remove()
        document.removeEventListener('mousedown', onMenuShowing)   //移除创建菜单时的全局监听
    }
    // 处理子组件发送的删除事件
    root.addEventListener('remove', () => {
        removeRoot()
    })

    function onMenuShowing(event) {
        if (!root.contains(event.target)) {   //点击了菜单外部
            removeRoot()
        }
    }

    document.addEventListener('mousedown', onMenuShowing)

    event.preventDefault()

}

export {YQContextMenu}