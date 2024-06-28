<template>
	<view class="apex-page">
		<view class="header">
			<text class="apex-title">Apex</text>
		</view>
		<scroll-view class="main">
			<view class="legend-selector">
				<text class="selector-title">Choose Your Legend</text>
			</view>
		</scroll-view>
		<view class="container">
				<button class="transparent-button" @click="go">开始识别</button>
		</view>
		
		<view class="footer">
			<a href="https://www.ea.com/games/apex-legends?isLocalized=true">© 2023 Respawn Entertainment. All rights reserved.</a>
		</view>
	</view>
</template>

<script setup>
	import {ref} from "vue"

	let go=()=>{
		uni.switchTab({
			url:'/pages/legend/legend'
		})
	}
</script>

<style lang="scss" scoped>
	.apex-page{
		background-image: url('../../static/images/apex-background1.jpg');
		background-size: cover;
		display: flex;
		flex-direction: column;
		height: 100vh;
	}
	.header,.footer{
		padding: 30rpx;
		text-align: center;
	}
	
	.apex-title{
		color: #FFD70;
		font-size: 36rpx;
	}
	.main{
		flex:1;
		overflow: auto;
	}
	.selector-title{
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
	}
	.legend-list{
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
	}
	.legend-item{
		width: 30%;
		padding: 20rpx;
		text-align: center;
	}
	.legend-image{
		width: 100%;
		height: 200rpx;
		border-radius: 10rpx;
		margin-bottom: 10px;
	}
	.legend-name{
		color: #FFD700;
		font-size: 24rpx;
	}
	.legend-description{
		color: #fff;
		font-size: 16rpx;
	}
	.transparent-button {
	  /* 设置按钮背景为透明 */
	  background-color: transparent;
	  /* 可选：调整文字颜色以适应透明背景 */
	  color: #000;
	  /* 可选：增加其他样式，如字体大小、圆角等 */
	  font-size: 16px;
	  cursor: pointer;
	  /* 为了美观和触摸反馈，可以添加一些伪类样式 */
	  &:active {
	    opacity: 0.8; /* 点击时稍微变暗 */
	  }
	}
</style>
