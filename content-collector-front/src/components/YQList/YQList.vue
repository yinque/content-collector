<script setup>

</script>

<template>
  <div class="yq-list mid yellow">
      <slot></slot>
  </div>
</template>

<style scoped>
.yq-list{
  overflow-y: scroll;
}
</style>

<script>
export default {
  name: "YQList"
}
</script>