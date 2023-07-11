<script setup>
import {nextTick, ref, watch} from "vue";

const props = defineProps(['modelValue'])
defineEmits(['update:modelValue'])


const textarea = ref()

// 自适应高度
watch(() => props.modelValue, () => {
  nextTick(() => {
    textarea.value.style.height = 'auto'
    textarea.value.style.height = `${textarea.value.scrollHeight}px`;
  })
})
</script>
<template>
  <div class="yq-textarea">
    <textarea
        ref="textarea"
        v-bind="$attrs"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
    >
    </textarea>
  </div>
</template>

<script>
export default {
  name: "YQTextarea"
}
</script>

<style scoped>

</style>