import {createRouter, createWebHistory} from 'vue-router';

import Home from './views/Home.vue'
import NoteEdit from './views/NoteEdit.vue'
import Test from './views/Test.vue'


const routes = [
    {path: '/', component: Home},
    {path: '/edit', component: NoteEdit},
    {path: '/edit/:id', component: NoteEdit},
    {path: '/test', component: Test}
]

const router = createRouter({
    // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
    history: createWebHistory(),
    routes, // `routes: routes` 的缩写
})

export default router