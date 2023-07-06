<script lang="ts" setup>
import {defineProps} from "vue";


const props = defineProps({
  type: {
    type: String as () => ('new' | 'save'),
    default: 'new'
  }
})
</script>
<template>
  <button type="button" :class="props.type"></button>
</template>

<script lang="ts">
export default {
  name: "YQButton"
}
</script>

<style lang="scss" scoped>
button{
  position: fixed;
  bottom: 1em;
  right: 1em;
  font-size: 1.5em;
  $size:2em;
  line-height: $size;
  width: $size;
  border: none;
  border-radius: 50%;
  color: white;
  background-color: #FEC013;
  user-select: none;
  transition: box-shadow 1s ease;
  $bs:0px 8px 16px 0px rgba(0, 0, 0, 0.15);
  box-shadow: $bs;
&:active{
 }
&:hover{
   cursor: pointer;
   box-shadow: -12px -8px 40px rgba(70,70,70,0.12) inset
   ,$bs;
 }
}

button.new::after{
  content: '+';
}
button.save::after{
  content: '☑';
}
</style>