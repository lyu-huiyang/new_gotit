New gotit
=========
校内信息查询平台(教务处升级后gotit重写)

[http://lvhuiyang.cn](http://lvhuiyang.cn)(目前正使用个人域名测测试)

帮助同学使用正方教务系统、图书馆以及计算学分绩点等功能。

##功能组件

+ 在线查询教务系统成绩
+ 在线查询教务系统课表
+ 绩点以及综合成绩查询
+ 图书借阅明细查询
+ 微信公众账号


## 程序运行环境

+ python2.7
+ redis
+ mongodb



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
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

##项目目录结构
```
new_gotit/                           # 项目根目录
├── app/                             # 项目的程序单元
│   ├── jwc/                         # 综合成绩以及绩点查询模块
│   │   ├── __init.py                # 模块初始化文件
│   │   ├── computer.py              # 计算绩点
│   │   ├── jwc.py                   # 视图函数
│   │   ├── spider                   # 爬虫文件
│   │   └── wechat.py                # 微信端视图函数
│   ├── library/                     # 图书馆模块
│   │   ├── __init.py                # 模块初始化文件
│   │   ├── library.py               # 视图函数以及爬虫
│   │   ├── test.py                  # 测试以及提供API返回JSON
│   │   └── wechat.py                # 微信端视图函数
│   ├── static/                      # 项目的静态文件，包括css, js等
│   │   ├── content/                 
│   │   ├── fonts/                   
│   │   ├── scripts/                 
│   │   ├── bootstrap.min.css        
│   │   └── home.css                 
│   ├── templates/                   # 项目模板文件(html页面)
│   │   ├── about.html               
│   │   ├── ''''''                   
│   │   └── wechat_library.html      
│   ├── zhengfang/                   # 正方教务系统查成绩的模块
│   │   ├── __init.py                # 模块初始化文件
│   │   ├── get_random_str.py        # 根据时间提供不相同的随机数组成的字符串，用以命名验证码
│   │   ├── no_input_query.py        # 微信端实现一键查询的视图函数
│   │   ├── wechat.py                # 微信端视图函数
│   │   └── zhengfang.py             # 视图函数以及爬虫
│   ├── zhengfang_class/             # 正方教务系统查课表的模块
│   │   ├── __init.py                # 模块初始化文件
│   │   ├── class_test.py            # 测试
│   │   ├── class_with_requests.py   # 视图函数以及爬虫(使用的是requests库)
│   │   ├── no_input_query.py        # 微信端实现一键查询的视图函数
│   │   ├── get_random_str.py        # 根据时间提供不相同的随机数组成的字符串，用以命名验证码
│   │   ├── wechat.py                # 微信端视图函数
│   │   └── zhengfang_class.py       # 视图函数以及爬虫
│   ├── __init__.py                  # 项目的整个程序单元初始文件
│   ├── db_operating.py              # 用以连接mongodb数据库以及提供函数操作
│   ├── form.py                      # 表单
│   ├── index.py                     # 首页视图函数
│   └── wechat_index.py              # 微信基本功能操作
├── .gitignore                       # git忽略文件
├── README.md                        # README
├── manage.py                        # 测试运行文件
└── requirements.txt                 # 程序依赖需求文件
```
