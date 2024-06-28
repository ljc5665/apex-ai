<template>
	<view class="apex-legends-container">
	  <view class="header">
	    <text class="title">Apex Legends Guns</text>
	  </view>
	  <scroll-view scroll-y class="legends-list">
		  <view class="box">
	    <view v-for="gun in guns" class="legend-card">
	      <image :src="gun.image" class="legend-image" mode="aspectFit" @click="show(gun)"/>
	      <view class="legend-info">
			  <view class="legend-role">{{ gun.category}}</view>
	      </view>
	    </view>
		</view>
	  </scroll-view>
		<navigator url="../index/identify2/identify2">
			<image class="c" src="../../static/AI.png"></image>
		</navigator>
	</view>
</template>

<script setup>
import {ref} from 'vue'

let guns =ref([{
		name: "R-99",
		category: "Submachine Gun",
		image: "../../static/images/R991.png",
		description: "A rapid-firing submachine gun with an incredibly high rate of fire, making it deadly in close quarters combat, but requiring careful management of its ammo due to its voracious appetite for rounds.",
	}
	,{
		name: "Sentinel",
		category: "Sniper Rifle",
		image: "../../static/images/Sentinel.png",
		description: "A powerful bolt-action sniper rifle known for its ability to deal massive damage with pinpoint accuracy. Its unique feature, the Charge Shot, allows players to charge up shots for increased penetration power, capable of piercing through both shields and body armor with a single well-placed hit, at the cost of slower firing rate.",
	}
	,{
		name: "Peacekeeper",
		category: "Shotgun",
		image: "../../static/images/Peacekeeper.png",
		description: "A reliable and versatile semi-automatic shotgun, the Peacekeeper excels in close-range engagements with its tight spread and high damage output per pellet. Its reputation stems from its ability to down enemies swiftly with precise aiming, making it a popular choice among players who prefer aggressive playstyles in confined spaces.",
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
		bottom: 1120rpx;
		right: 650rpx;
		width: 70rpx;
		height: 70rpx;

	}

.apex-legends-container {
  width: 750rpx;
  height: 1170rpx;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-image: url('../../static/images/6.jpg'); /* 替换为你的背景图片路径 */
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
