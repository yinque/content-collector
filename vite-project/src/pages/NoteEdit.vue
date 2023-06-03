<script setup>

import YQButton from "../components/YQButton.vue";
import {onMounted, reactive} from "vue";
import note_api from "../api/index";

import { useRoute } from 'vue-router';
import YQTextarea from "../components/YQTextarea.vue";
const route = useRoute()

const editor = reactive({
  title:"",
  content:""
})
const id = route.params.id?String(route.params.id):null
onMounted(async ()=>{
  if(id){
    const note = await note_api.get_note_by_id(id)
    Object.assign(editor,note)
  }
})

function currentDate(){
  const date = new Date();

  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  const seconds = String(date.getSeconds()).padStart(2, '0');

  const formattedDate = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
  // console.log(formattedDate); // 例如：2023-05-25 12:30:22
  return formattedDate

}
function submit(){
  if(id){  //编辑笔记
    note_api.update_note(id, {...editor,modify_time:currentDate()})
  }else{  //新建笔记
    note_api.create_note({...editor,modify_time:currentDate()})
  }

}

</script>
<template>
    <h2>编辑器</h2>
    <div class="note-editor">
        <header>
            <YQTextarea class="title"
                        placeholder="标题..."
                        rows="1"
                        v-model="editor.title"
                        ref="title">

            </YQTextarea>
        </header>
        <main>
            <YQTextarea class="content"
                        placeholder="内容..."
                        v-model="editor.content"
                        ref="content">
            </YQTextarea>
        </main>
    </div>
    <YQButton @click="submit" type="save"></YQButton>
</template>

<script>
export default {
  name: "NoteEdit"
}
</script>

<style lang="scss" scoped>

.note-editor{
  padding: 1em;
  .title{
    width: 100%;
    margin-bottom: 0.5em;
    font-size: 1.1em;
    font-weight: bold;
  }
  .content{

  }
}
textarea {
  width: 100%;
  border: 1px solid #ccc;
  background-color: #f5f5f5;
  resize: none;
}
</style>