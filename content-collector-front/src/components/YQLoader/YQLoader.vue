<script setup>
/*
 * References:
 * - Animation: https://codepen.io/CKH4/pen/ZGNyep/
 */
const props = defineProps({
  size: {
    type: String,
    default: "20px"
  }
})
</script>

<template>
  <div class="yq-loader" :style="`--dot-size: ${props.size}`">
    <div class="loader">
      <div class="dot" v-for="i in Array(5)"></div>
    </div>
  </div>
</template>

<style lang="stylus" scoped>
//.yq-loader
//  --dot-size: 12px
.loader
  position absolute
  top 50%
  left 40%
  margin-left 10%
  transform translate3d(-50%,-50%,0)

.dot
  width var(--dot-size)
  height var(--dot-size)
  background #3ac
  border-radius 100%
  display inline-block
  animation slide 1s infinite

for n in (1..5)
  .dot:nth-child({n})
    animation-delay (.1s * n)
    background red(#3ac, (50 * n))

@keyframes slide
  0%
    transform scale(1)
  50%
    opacity .3
    transform scale(2)
  100%
    transform scale(1)
</style>

<script>
export default {
  name: "YQLoader"
}
</script>