<script lang="ts" setup>
import {defineProps} from "vue";

interface Note{
  "id": number,
  "title": string,
  "content": string,
  "modify_time": string
}
const props = defineProps<{
  note: Note
}>()
</script>
<template>
  <div class="note">
      <main>
          <div class="content" @click="$router.push('/edit/'+props.note.id)">{{props.note.content}}</div>
      </main>
      <footer>
          <div class="modify_time">{{props.note.modify_time}}</div>
      </footer>
  </div>
</template>


<style lang="scss" scoped>
.note{
    margin-bottom: 1em;
    padding: 0.5em;
}
.note{
    background-color: white;
    border: 1px solid #EEE;
    border-radius: 0.5em;
    box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.075);
    .content{
       display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 3;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .modify_time{
        font-size: 0.5em;
        color: #7E7E7E;
        margin-top: 0.5em;
    }
}
</style>