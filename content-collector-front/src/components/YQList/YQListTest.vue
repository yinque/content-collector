<script setup>

import YQList from "./YQList.vue";
import YQListItem from "./YQListItem.vue";
import {note_api} from "../../api/index";
import {onMounted} from "vue";

class NoteDataProcess{
  constructor() {

  }
}
onMounted(async ()=>{
  const ndp = new NoteDataProcess()
})
</script>

<template>
  <div class="yq-list-test">
    YQListTest
    <YQList>
      <YQListItem v-for="i in Array(10)"></YQListItem>
    </YQList>
  </div>
</template>

<style scoped>
</style>

<script>
export default {
  name: "YQListTest"
}
</script>