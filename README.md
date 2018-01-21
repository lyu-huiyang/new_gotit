New gotit（该项目已停止维护）
=========
校内信息查询平台(教务处升级后gotit重写)

帮助同学使用正方教务系统、图书馆以及计算学分绩点等功能。

## 功能组件

+ 在线查询教务系统成绩
+ 在线查询教务系统课表
+ 绩点以及综合成绩查询
+ 图书借阅明细查询
+ 微信公众账号


## 程序运行环境

+ python 3.5
+ redis 3.0.6
+ mysql-server-5.7



## 安装所需依赖
```
apt-get install python-virtualenv             # 安装python虚拟环境
virtualenv venv                               # 创建名为venv的python虚拟环境
source venv/bin/activate                      # 使用虚拟环境
(venv)pip install -r `requirements.txt`        # 在虚拟环境下安装程序所需依赖
```
##启动方式
```
# 测试运行
python manage.py

# 正式上线
gunicorn -w 4 -b 0.0.0.0:80 manage:app
```

