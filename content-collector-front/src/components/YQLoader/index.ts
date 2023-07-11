/*
加载组件
 */
import YQLoader from "./YQLoader.vue";
import {createApp, h} from "vue";

export class Loader{
    // 创建挂载元素
    root = document.createElement('div');
    // 创建app
    app = createApp(() => h(YQLoader, {
    }));

    constructor(target: Element) {
        this.root.style.width="100%"
        this.root.style.height="100%"
        this.root.style.position="relative"
        target.appendChild(this.root)

        // 渲染组件到root元素上
        this.app.mount(this.root)
    }
    destroy(){
        this.root.remove()
        this.app.unmount()
    }
}

// export function bindLoading(target: Element){
//     // 目标元素创建app容器
//     const root = document.createElement('div')
//     root.style.width="100%"
//     root.style.height="100%"
//     root.style.position="relative"
//     target.appendChild(root)
//     // 创建app
//     const app = createApp(() => h(YQLoader, {
//     }))
//     // 渲染组件到root元素上
//     app.mount(root)
// }


