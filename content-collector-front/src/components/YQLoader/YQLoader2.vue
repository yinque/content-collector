<script setup>
/*
 * References:
 * - Animation: https://codepen.io/redouglas/pen/rNRbzV
 */
</script>

<template>
  <div class="yq-loader2">
    <div class="loader">
      <div class="side"></div>
      <div class="side"></div>
      <div class="side"></div>
      <div class="side"></div>
      <div class="side"></div>
      <div class="side"></div>
      <div class="side"></div>
      <div class="side"></div>
    </div>
  </div>
</template>

<style lang="stylus" scoped>
$side-length = 20px
$side-width = 6px
$side-color = #046380
$loader-size = $side-length * (1 + math(2, 'sqrt'))

$anim-duration = 1.5s
$anim-offset = 0

.loader
  position: absolute
  left: 50%
  top: 50%
  width: $loader-size
  height: $loader-size
  margin-left: ($loader-size / -2)
  margin-top: ($loader-size / -2)
  border-radius: 100%
  animation-name: loader
  animation-iteration-count: infinite
  animation-timing-function: linear
  animation-duration: 4s

  .side
    display: block
    width: $side-width
    height: $side-length
    background-color: $side-color
    margin: 2px
    position: absolute
    border-radius: 50%
    animation-duration: $anim-duration
    animation-iteration-count: infinite
    animation-timing-function: ease

    &:nth-child(1), &:nth-child(5)
      transform: rotate(0deg)
      animation-name: rotate0
    &:nth-child(3), &:nth-child(7)
      transform: rotate(90deg)
      animation-name: rotate90
    &:nth-child(2), &:nth-child(6)
      transform: rotate(45deg)
      animation-name: rotate45
    &:nth-child(4), &:nth-child(8)
      transform: rotate(135deg)
      animation-name: rotate135

  for count in (0..7)
    .side:nth-child({count + 1})
      $side-offset = ($side-width / 2) * count
      $dotval = ($loader-size / 2)

      top: sin(45deg * count) * $dotval + $dotval
      left: cos(45deg * count) * $dotval + $dotval
      margin-left: ($side-width / -2)
      margin-top: ($side-length / -2)
      animation-delay: $anim-offset * count

// side keyframes
@keyframes rotate0
  0%
    transform: rotate(0deg)
  60%
    transform: rotate(180deg)
  100%
    transform: rotate(180deg)

@keyframes rotate90
  0%
    transform: rotate(90deg)
  60%
    transform: rotate(270deg)
  100%
    transform: rotate(270deg)

@keyframes rotate45
  0%
    transform: rotate(45deg)
  60%
    transform: rotate(225deg)
  100%
    transform: rotate(225deg)

@keyframes rotate135
  0%
    transform: rotate(135deg)
  60%
    transform: rotate(315deg)
  100%
    transform: rotate(315deg)

// loader keyframe
@keyframes loader
  0%
    transform: rotate(0deg)
  100%
    transform: rotate(360deg)

</style>

<script>
export default {
  name: "YQLoader2"
}
</script>