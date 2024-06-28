<template>
	<view>
		<scroll-view class="scroll_box" :scroll-top="y" scroll-y="true">
			<view class="box">
				<view v-for="el in arr">

					<view class="leftbox" v-if="el.num==0">
						<image class="touxiang" :src="el.img"></image>
						<view v-if="el.flag==0" class="chattext">{{el.text}}</view>
						<image v-else-if="el.flag==1" class="chating" :src="el.connect"></image>
					</view>
					<view class="rightbox" v-if="el.num==1">
						<view v-if="el.flag==2" class="chattext">{{el.text}}</view>
						<image v-else-if="el.flag==3" class="chating" :src="el.connect"></image>
						<image class="touxiang" :src="el.img"></image>
					</view>

				</view>

				
			</view>
		</scroll-view>
		<view class="bottomabar">
			<input class="chatinput" type="text"  v-model="chattext" />
			<view class="sendbtn" @click="send">发送</view>

		</view>
		<image class="c" src="../../../static/camera.png" @click="send2" mode=""></image>
	</view>

</template>

<script setup>
	import {
		ref,
		nextTick
	} from "vue"

	let arr = ref([{
			flag: 0,
			text: "你好，我是Pathfinder",
			img: "../../../static/images/3.jpg",
			num: 0
			}
			,{
				flag:0,
				text:"请发送你想要检测的传奇",
				img:"../../../static/images/3.jpg",
				num:0
			}
		// }, {
		// 	flag: 1,
		// 	connect: "../../../static/images/1.jpg",
		// 	img: "../../../static/images/3.jpg",
		// 	num: 0

		// }, {
		// 	flag: 2,
		// 	text: "你好，我是Horizon",
		// 	img: "../../../static/images/2.jpg",
		// 	num: 1
		// }, {
		// 	flag: 3,
		// 	connect: "../../../static/images/1.jpg",
		// 	img: "../../../static/images/2.jpg",
		// 	num: 1

		// }

	])
	let y = ref(999999999)
	let chattext = ref("")
	let send = () => {
		// chattext.value="修改了,但是这个技术是响应式数据"
		//获取输入框中的数据
		console.log(chattext.value)
		let msg=chattext.value
		//把用户输入的数据处理成数组中需要的格式
		let obj1 = {
			flag: 2,
			text: chattext.value,
			img: "../../../static/images/2.jpg",
			num: 1 
		}
		//发送到滚动条上面去
		arr.value.push(obj1)
		// y.value=y.value+1
		nextTick(() => {
			//等上面的把数据刷新到页面上的渲染操作执行完毕后才会调用这个函数
			//把滚动条滚下来
			y.value = y.value + 1
			chattext.value=""//输入框清空
		})


		//发送给服务器
		console.log(msg,"==========")
		
		uni.request({
			url:"http://localhost:7001/ernie",//给哪个服务器发送
			method: "POST",
			header: {
			        "Content-Type": "application/json"
			        },
			data:{text:msg},
			success: (res) => {
				console.log(res.data.result,"服务器返回值")
				let obj2={
					flag:0,
					text:res.data.result,
					img:"../../../static/images/3.jpg",
					num:0
				}
				arr.value.push(obj2)
				
				nextTick(()=>{
					y.value = y.value + 1
				})
			}
		})
		
	}
	let chatimg=ref("")
	let send2=()=>{
		uni.chooseImage({
			success(f) {
				console.log(f.tempFilePaths[0])
				//前端预览
				chatimg.value=f.tempFilePaths[0]
				let msg=chatimg.value
				//把用户输入的数据处理成数组中需要的格式
				let obj1 = {
					flag: 3,
					connect: chatimg.value,
					img: "../../../static/images/2.jpg",
					num: 1 
				}
				//发送到滚动条上面去
				arr.value.push(obj1)
				// y.value=y.value+1
				nextTick(() => {
					//等上面的把数据刷新到页面上的渲染操作执行完毕后才会调用这个函数
					//把滚动条滚下来
					y.value = y.value + 1
				})
				
				//3.把图片发送给服务器
				uni.uploadFile({
					url:"http://localhost:5000/legends",
					filePath:f.tempFilePaths[0],
					name:"faceimg",
					success(res){
						console.log("========后端返回")
						
						let obj3={
							flag:0,
							text:"已成功识别，这个英雄是："+JSON.parse(res.data).legends_name,
							img:"../../../static/images/3.jpg",
							num:0
						}
						let obj2={
							flag:1,
							connect:JSON.parse(res.data).url,
							img:"../../../static/images/3.jpg",
							num:0
						}
						arr.value.push(obj2)
						arr.value.push(obj3)
						
						nextTick(()=>{
							y.value = y.value + 1
						})
					}
				})
			}
		})
	}
	
	//返回结果也显示到滚动上面去
</script>

<style>
	.chattext {
		min-width: 200rpx;
		background-color: chartreuse;
		max-width: 550rpx;
		padding: 15rpx;
		font-size: 24rpx;
		border-radius: 20rpx;
		margin-bottom: 12rpx;
		word-break: break-all;
	}

	.rightbox.chattext {
		border-radius: 10rpx 0rpx 10rpx 0rpx;
		background-color: aliceblue;
	}

	.scroll_box {
		width: 750rpx;
		height: 1170rpx;
		/* background-color: rgb(240, 240,240); */
		background-image: url("../../../static/images/5.jpg");
/* 		background-size: 750rpx 1120rpx; */
		background-size: cover; /* 图片覆盖容器 */
		background-position: center center; /* 图片居中 */
		background-repeat: no-repeat; /* 防止图片重复 */
		background-attachment: fixed; /* 固定背景，不随滚动条滚动 */
		position: relative; /* 用于后续可能的叠加元素定位 */
	}

	.bottomabar {
		width: 750rpx;
		height: 72rpx;
		background-color: whitesmoke;
		flex-wrap: nowrap;
		display: flex;
		justify-content: flex-start;


	}

	.chatinput {
		background-color: white;
		width: 650rpx;
		height: 70rpx;
		margin-top: 6rpx;
		border-radius: 10rpx 0rpx 0rpx 10rpx;
		padding-left: 10rpx;
		font-size: 28rpx;
	}

	.sendbtn {
		background-color: brown;
		width: 100rpx;
		height: 70rpx;
		margin-top: 6rpx;
		border-radius: 0rpx 10rpx 10rpx 0rpx;
		padding-left: 10rpx;
		font-size: 28rpx;
		line-height: 70rpx;
		text-align: center;
		padding-left: 0rpx;
	}

	.c {
		position: fixed;
		bottom: 5rpx;
		right: 110rpx;
		width: 45rpx;
		height: 50rpx;

	}

	.box {
		width: 400rpx;
		height: 700rpx;

	}

	.rightbox {
		width: 750rpx;
		display: flex;
		justify-content: flex-end;
		flex-wrap: nowrap;
		padding-top: 20rpx;
	}


	.leftbox {
		width: 750rpx;
		display: flex;
		justify-content: flex-start;
		flex-wrap: nowrap;
		padding-top: 20rpx;
	}

	.touxiang {
		width: 60rpx;
		height: 60rpx;
		border-radius: 30rpx;
		margin-right: 10rpx;
		margin-left: 20rpx;
	}

	.chating {
		width: 500rpx;
		height: 300rpx;
		border-radius: 20rpx;
	}
	.leftbox .chattext {
	        background-color: white;
	    }
</style>