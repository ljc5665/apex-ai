<template>
	<view class="apex-legends-container">
	  <view class="header">
	    <text class="title">Apex Legends Badges</text>
	  </view>
	  <scroll-view scroll-y class="legends-list">
		  <view class="box">
	    <view v-for="badge in badges" class="legend-card">
	      <image :src="badge.image" class="legend-image" mode="aspectFit" @click="show(badge)"/>
	      <view class="legend-info">
			  <view class="legend-role">{{ badge.name}}</view>
	      </view>
	    </view>
		</view>
	  </scroll-view>
		<navigator url="../index/identify3/identify3">
			<image class="c" src="../../static/AI3.png"></image>
		</navigator>
	</view>
</template>

<script setup>
import {ref} from 'vue'

let badges =ref([{
		name: "Predator Medal",
		image: "../../static/images/Predator Medal.jpg",
		description: "Awarded to players who demonstrate exceptional hunting skills by eliminating an entire squad of enemies single-handedly within a short timeframe, showcasing prowess, strategy, and swift execution on the battlefield in Apex Legends.",
	}
	,{
		name: "Dual Demolisher Tag",
		image: "../../static/images/Dual Demolisher Tag.jpg",
		description: "Earned by players in Apex Legends when they expertly knock down two adversaries virtually at once, illustrating superior aiming proficiency, swift tactical judgment, and a capacity to impose dominance on the battlefield through rapid and successive takedowns",
	}
	,{
		name: "Skull Sea Patch",
		image: "../../static/images/Skull Sea Patch.jpg",
		description: "Bestowed upon Apex Legends players who amass an impressive count of eliminations during a single match, signifying their fearsome prowess, relentless aggression, and unmatched lethality that leaves behind a trail of defeated foes reminiscent of a sea of skulls.",
}
	
])

let show=(gun)=>{

	 // ImageDetailsPopup.open(apexLegends);
	 uni.showModal({
	 	title:gun.name,
		content:gun.description,
		showCancel:false,
	 })
}

</script>

<style lang="scss" scoped>
.box {
		width: 400rpx;
		height: 700rpx;
	
	}
	
.c {
		position: fixed;
		bottom: 1130rpx;
		right: 680rpx;
		width: 70rpx;
		height: 70rpx;

	}

.apex-legends-container {
  width: 750rpx;
  height: 1170rpx;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-image: url('../../static/images/7.jpg'); /* 替换为你的背景图片路径 */
  background-size: cover; /* 图片覆盖容器 */
  background-position: center center; /* 图片居中 */
  background-repeat: no-repeat; /* 防止图片重复 */
  background-attachment: fixed; /* 固定背景，不随滚动条滚动 */
  position: relative; /* 用于后续可能的叠加元素定位 */
}

.header {
  padding: 20px;
  text-align: center;
}

.title {
  font-size: 28px;
  color: #FFD700;
}

.legends-list {
  width: 750rpx;
  height: 1170rpx;
  flex: 1;
  padding: 20px 20px;
}

.legend-card {
  background-color: rgba(255, 255, 255, 0);
  border-radius: 10px;
  padding: 20rpx 20rpx 20rpx 20rpx;
  margin-bottom: 20px;
  width: 750rpx;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.legend-image {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  margin-bottom: 20px;
}

.legend-info {
  text-align: center;
}

.legend-name {
  font-size: 24px;
  color: #ffffff;
  margin-bottom: 5px;
}

.legend-role {
  font-size: 16px;
  color: #FFD700;
  margin-bottom: 5px;
}

.legend-description {
  font-size: 14px;
  color: #ffffff;
  text-align: justify;
  width: 80%;
}
</style>
