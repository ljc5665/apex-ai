<template>
  <view class="apex-legends-container">
	<view class="header">
      <text class="title">Apex Legends Characters</text>
    </view> 
    <scroll-view scroll-y class="legends-list">
	<view class="box">
      <view v-for="legend in apexLegends" class="legend-card">
        <image :src="legend.image" class="legend-image" mode="aspectFit" @click="show(legend)"/>
        <view class="legend-info">
		  <view class="legend-role">{{ legend.role}}</view>
        </view>
      </view>
	  </view>
    </scroll-view>
	
	<navigator url="../index/identify/identify">
		<image  class="c" src="../../static/AI2.png"></image>
	</navigator>
  </view>
</template>

<script setup>
import { ref } from 'vue';
// import ImageDetailsPopup from '../ImageDetailsPopup/ImageDetailsPopup.vue'; // 引入图片详情弹窗组件
// 示例数据，实际应用中可能需要从API获取
const apexLegends = ref([
  {
    name: 'Valkyrie',
    role: 'Aggressive Recon',
    description: 'A fierce pilot equipped with jetpacks that allow for rapid aerial maneuvers, Valkyrie can rain down rockets and soar above the battlefield to scout and ambush enemies from above.',
    image: '../../static/images/Valkyrie.jpg', 
  },
  // 更多传奇数据...
  {
	name: 'Horizon',
	role: 'Scientist',
	description: 'A brilliant astrophysicist with the ability to manipulate gravity, creating micro black holes and harnessing energy fields to outmaneuver opponents.',
	image: '../../static/images/Horizon.jpg',   
  },{
	name: 'Octane',
	role: 'High-Speed Agility',
	description: 'A thrill-seeking adrenaline junkie, Octane relies on his swift speed and self-healing abilities to outmaneuver opponents and stay in the fight. With a personal jump pad and stim注射器 that grants him unmatched mobility, he’s always ready for the next high-speed chase.',
	image: '../../static/images/Octane.jpg',
  },{
	name: 'Revenant',
	role: 'Assassin',
	description: 'Once a feared mercenary, Revenant is now an undead assassin with enhanced agility and a chilling presence on the battlefield. Equipped with a silenced weapon and the ability to turn invisible while moving swiftly, he excels at stalking prey and executing them with deadly precision. His ultimate allows him to deploy a terrifying death machine that hunts down targets autonomously." creates a pair of portals allowing her squad to rapidly escape or initiate ambushes from unexpected angles.',
	image: '../../static/images/Wraith.jpg',
  }
]);

let show=(legend)=>{

	 // ImageDetailsPopup.open(apexLegends);
	 uni.showModal({
	 	title:legend.name,
		content:legend.description,
		showCancel:false,
	 })
}


// 你可以在此处添加更多逻辑，比如点击传奇卡片查看详细信息的功能
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
  background-image: url('../../static/images/4.jpg'); /* 替换为你的背景图片路径 */
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