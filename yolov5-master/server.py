#djiango
# flask
from flask import Flask, request, jsonify
import os
import cv2

from flask_cors import CORS
import detect as yolov5_detect
import time

#http://ip:port/pathname?querysrting
#static_folder='runs/detect' 去服务器电脑的哪个路径中读取静态资源

#static_url_path="/" 客户端访问的pathname
app = Flask(__name__,static_folder='runs/detect',static_url_path="/")
CORS(app)#跨域资源共享

#注册路径（网址）
#router.post('/ss',func) egg
@app.route('/detect', methods=['POST'])
def detect_objects():
    #request 是客户端发送过来的数据包:request.files是文件 是一个字典

    # 检查是否有文件上传
    # if 'file' not in request.files:
    #     return jsonify({'error': 'No file part'}), 400

    file = request.files['faceimg']
    #file 是前端发送过来的图片对应的对象
    # file.filename 是文件的名字
    # file.save(path) 把文件保存到path路径中

    # 检查文件是否为空
    # if file.filename == '':
    #     return jsonify({'error': 'No selected file'}), 400

    # 保存上传的资源到临时文件
    # path = os.path.join("temp", file.filename)
    # file.save(path)

    path=file.filename
    file.save(path)#把图片保存到当前文件夹下


    t=time.time()#一串数字 是时间戳
    # 调用YOLOv5进行检测
    output_video_path = yolov5_detect.run(weights='yolov5s.pt',  # 指定模型权重
                                          source=path,
                                          #vid_stride=1, # 视频帧率步长
                                          # save=True,
                                          # project="detections",
                                          name=f'exp{t}',  # 使用无扩展名的文件名作为输出目录
                                          # exist_ok=True,
                                          device='cpu')  # 设备，如'cpu'或'0'表示GPU




    # 清理临时文件
    os.remove(path)
    # 返回处理后的视频路径或者直接处理为视频流返回（这一步需要更详细的实现）
    return f'http://localhost:5000/exp{t}/{file.filename}'


if __name__ == '__main__':
    app.run(debug=True)
