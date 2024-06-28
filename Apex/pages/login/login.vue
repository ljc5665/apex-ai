<template>
  <view class="login-container">
    <view class="logo-container">
      <image src="../../static/images/apex-bg4.jpg" mode="widthFix" class="apex-logo" />
    </view>
   <view class="form-container">
      <input type="text" placeholder="账号" class="input-field" />
      <input type="password" placeholder="密码" class="input-field" />
	  <image src="../../static/images/login.jpg" class="login-img" @click="login"></image>
   </view>
  </view>
</template>

<script setup>
	import {ref} from 'vue';
	
	let username = ref('');
	let password = ref('');
	
	async function login() {
	  try {
	    const response = await axios.post('http://your-backend-api-url/login', {
	      username: username.value,
	      password: password.value
	    });
	
	    if (response.data.success) {
	      console.log('登录成功');
	      // 保存token或执行登录成功后的操作，如跳转页面
	    } else {
	      console.error('登录失败:', response.data.message);
	    }
	  } catch (error) {
	    console.error('登录请求失败:', error);
	  }
	}
</script>

<style lang="scss" scoped>
.login-img{
	width: 50%;
	height: 70rpx;
	margin-left: 130rpx;
}
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: rgb(192, 48, 41); /* Apex风格的深色背景 */
  background-image: url("../../static/images/apex-login2.jpg");
  background-repeat: repeat;
  background-size: 100% 100%;
}

.logo-container {
  margin-bottom: 30px;
}

.apex-logo {
    width: 200px;
    height: auto;
	background-color: transparent;
	border: none;
}

.form-container {
  width: 80%;
  max-width: 400px;
  padding: 20px;
  background-color: rgb(62, 0, 9); /* 较深的背景以便区分 */
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  border: none;
}

.input-field {
  background-color: #383c45;
  color: white;
  padding: 12px;
  margin-bottom: 15px;
  border-radius: 5px;
  border: none;
}

.login-button {
  background-color: rgb(167, 6, 11); /* Apex的标志性橙色 */
  color: white;
  padding: 12px;
  border: none;
  text-align: center;
  width: 50%;
  margin-bottom: 10px;
}

.forgot-password {
  color: #ea4a1f;
  text-align: right;
  margin-bottom: 10px;
}

.register-link {
  color: #ea4a1f;
  text-align: center;
}
</style>