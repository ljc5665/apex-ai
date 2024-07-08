# djiango 大型约定式
# flask 轻量级
import json

from flask import Flask, request, jsonify
import os
import cv2
import pymysql.cursors
from flask_cors import CORS
import time
import detect as yolov5_detect

#static_folder='runs/detect' 去服务器电脑的哪个路径中读取静态文件
#static_url_path="/" 客户端访问的pathname
app = Flask(__name__,static_folder='runs/detect',static_url_path="/")
#1.静态根目录  <=链接=>  2.前端url输入值
CORS(app)
# 跨域资源共享

#注册路径(网址)
@app.route('/legends', methods=['POST'])
def detect_legends():
    connect = pymysql.Connect(
        host='localhost',  # 主机名
        port=3306,  # 端口号
        user='root',
        passwd='root',  # 数据库的密码
        db='mysql',  # 要连接的数据库的名称
        charset='utf8'
    )
    cursor = connect.cursor()
    # 执行SQL查询
    cursor.execute('SELECT VERSION()')
    # 获取单条数据
    # request 是客户端发送过来的数据包 request.files是文件，是一个字典

    # 检查是否有文件上传
    # if 'file' not in request.files:
    #     return jsonify({'error': 'No file part'}), 400

    file = request.files['faceimg']  # 前端name属性取值
    # file 是前端发送过来的图片，对应的对象
    # file.filename 是文件的名字
    # file.save(path) 把文件保存到path路径中
    # 检查文件是否为空
    # if file.filename == '':
    #     return jsonify({'error': 'No selected file'}), 400

    # 保存上传的资源到临时文件
    # path = os.path.join("temp", file.filename)
    path = file.filename
    file.save(path)

    t=time.time()
    # 调用YOLOv5进行检测
    output_video_path = yolov5_detect.run(weights='legends.pt',  # 指定模型权重
                                          source=path,
                                          #vid_stride=1, # 视频帧率步长
                                          save_txt=True,
                                          # save=True,
                                          # project="detections",
                                          name=f'exp{t}',  # 使用无扩展名的文件名作为输出目录
                                          # exist_ok=True,
                                          device='cpu')  # 设备，如'cpu'或'0'表示GPU
    # 清理临时文件
    os.remove(path)
    sql = "SELECT name FROM apex_legends WHERE id='%s'"
    legends_name=""
    returnfile=os.path.splitext(path)[0]
    print(f'runs/detect/exp{t}/labels/{returnfile}.txt',"<=======识别后的文件")
    with open(f'runs/detect/exp{t}/labels/{returnfile}.txt', 'r') as mySqlFile:
        # 逐字读取文件内容
        first_char = mySqlFile.read(1)
        print(first_char,"<=============识别出的英雄id")
    data = (first_char,)  # 注意逗号（元组中只有一个元素的时候需要添加一个逗号）
    # print(sql % data)
    cursor.execute(sql % data)
    for row in cursor.fetchall():
        legends_name="%s" % row
        # print("%s\t" % row)
    print(legends_name,"识别出的英雄名字")
    # print("一共",cursor.rowcount, "条数据")
    # 关闭数据库连接
    connect.close()
    data={
        "legends_name":legends_name,
        "url":f'http://localhost:5000/exp{t}/{file.filename}'
    }
    # 返回处理后的视频路径或者直接处理为视频流返回（这一步需要更详细的实现）
    print(data)
    return jsonify(data)

@app.route('/guns', methods=['POST'])
def detect_guns():
    connect = pymysql.Connect(
        host='localhost',  # 主机名
        port=3306,  # 端口号
        user='root',
        passwd='root',  # 数据库的密码
        db='mysql',  # 要连接的数据库的名称
        charset='utf8'
    )
    cursor = connect.cursor()
    # 执行SQL查询
    cursor.execute('SELECT VERSION()')
    # 获取单条数据
    # request 是客户端发送过来的数据包 request.files是文件，是一个字典

    # 检查是否有文件上传
    # if 'file' not in request.files:
    #     return jsonify({'error': 'No file part'}), 400

    file = request.files['faceimg']  # 前端name属性取值
    # file 是前端发送过来的图片，对应的对象
    # file.filename 是文件的名字
    # file.save(path) 把文件保存到path路径中
    # 检查文件是否为空
    # if file.filename == '':
    #     return jsonify({'error': 'No selected file'}), 400

    # 保存上传的资源到临时文件
    # path = os.path.join("temp", file.filename)
    path = file.filename
    file.save(path)

    t=time.time()
    # 调用YOLOv5进行检测
    output_video_path = yolov5_detect.run(weights='gun.pt',  # 指定模型权重
                                          source=path,
                                          #vid_stride=1, # 视频帧率步长
                                          save_txt=True,
                                          # save=True,
                                          # project="detections",
                                          name=f'exp{t}',  # 使用无扩展名的文件名作为输出目录
                                          # exist_ok=True,
                                          device='cpu')  # 设备，如'cpu'或'0'表示GPU
    # 清理临时文件
    os.remove(path)
    sql = "SELECT name FROM apex_guns WHERE id='%s'"
    guns_name=""
    returnfile=os.path.splitext(path)[0]
    print(f'runs/detect/exp{t}/labels/{returnfile}.txt',"<=======识别后的文件")
    with open(f'runs/detect/exp{t}/labels/{returnfile}.txt', 'r') as mySqlFile:
        # 逐字读取文件内容
        first_char = mySqlFile.read(1)
        print(first_char,"<=============识别出的枪械id")
    data = (first_char,)  # 注意逗号（元组中只有一个元素的时候需要添加一个逗号）
    # print(sql % data)
    cursor.execute(sql % data)
    for row in cursor.fetchall():
        guns_name="%s" % row
        # print("%s\t" % row)
    print(guns_name,"识别出的枪械名字")
    # print("一共",cursor.rowcount, "条数据")
    # 关闭数据库连接
    connect.close()
    data={
        "guns_name":guns_name,
        "url":f'http://localhost:5000/exp{t}/{file.filename}'
    }
    # 返回处理后的视频路径或者直接处理为视频流返回（这一步需要更详细的实现）
    print(data)
    return jsonify(data)

@app.route('/badges', methods=['POST'])
def detect_badges():
    connect = pymysql.Connect(
        host='localhost',  # 主机名
        port=3306,  # 端口号
        user='root',
        passwd='root',  # 数据库的密码
        db='mysql',  # 要连接的数据库的名称
        charset='utf8'
    )
    cursor = connect.cursor()
    # 执行SQL查询
    cursor.execute('SELECT VERSION()')
    file = request.files['faceimg']  # 前端name属性取值
    path = file.filename
    file.save(path)
    t=time.time()
    # 调用YOLOv5进行检测
    output_video_path = yolov5_detect.run(weights='badges.pt',  # 指定模型权重
                                          source=path,
                                          #vid_stride=1, # 视频帧率步长
                                          save_txt=True,
                                          # save=True,
                                          # project="detections",
                                          name=f'exp{t}',  # 使用无扩展名的文件名作为输出目录
                                          # exist_ok=True,
                                          device='cpu')  # 设备，如'cpu'或'0'表示GPU
    # 清理临时文件
    os.remove(path)
    sql = "SELECT name FROM apex_badges WHERE id='%s'"
    badegesName=[]
    badges=[]
    returnfile=os.path.splitext(path)[0]
    print(f'runs/detect/exp{t}/labels/{returnfile}.txt',"<=======识别后的文件")
    with open(f'runs/detect/exp{t}/labels/{returnfile}.txt', 'r') as mySqlFile:
        # 逐字读取文件内容
        for line in mySqlFile:
            # 去除行尾的换行符并获取第一个字母
            badges.append(line.strip()[0])
        print(badges,"<=============识别出的英雄id")
    for i in badges:
        data = (i,)  # 注意逗号（元组中只有一个元素的时候需要添加一个逗号）
        # print(sql % data)
        cursor.execute(sql % data)

        for row in cursor.fetchall():
            badegesName.append("%s" % row)
    print(badegesName)
    # for name in badegesName:
    #     print(name)
    # print("一共",cursor.rowcount, "条数据")
    # 关闭数据库连接
    connect.close()
    data={
        "badges_name":badegesName,
        "url":f'http://localhost:5000/exp{t}/{file.filename}'
    }
    # 返回处理后的视频路径或者直接处理为视频流返回（这一步需要更详细的实现）
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
