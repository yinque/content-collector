<script setup>
  import Note from "../components/Note.vue";
  import YQButton from "../components/YQButton.vue";

  import note_api from '../api/index'
  import {onMounted, reactive} from "vue";

  const noteList = reactive([])
  onMounted(async ()=>{
    const notes = await note_api.get_all_notes()
    noteList.push(...notes)
  })
</script>
<template>
  <h2>笔记本</h2>
  <Note v-for="n in noteList" :note="n"></Note>
  <YQButton @click="$router.push('/edit')"></YQButton>
</template>

<script>
export default {
  name: "Home"
}
</script>

<style lang="scss" scoped>


</style>