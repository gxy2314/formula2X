## 1.项目介绍
&emsp;&emsp; 随着学术论文的数字化和在线共享的增加，数学公式作为学术内容的重要组成部分，其规范化复制和引用成为了一个重要问题。传统的图片，PDF等格式公式难以直接编辑和引用，这大大增加了研究工作的难度。基于对这一点的体会，我们设计了formula2X公式识别系统，旨在提供一个从数学公式图片到可编辑文本格式的自动化转换工具。项目采用django框架，基于深度学习模型，实现了web端的公式识别。用户可将包含公式的图片上传至web端，formula2X可实现图片中公式的识别，并将识别结果分别以markdown，latex等可复制呈现。
## 2. 项目结构
&emsp;&emsp;  `test.py`是测试模型的一个最小程序，`testforweb.py`用于查看django安装的情况</br>
&emsp;&emsp; `backend`文件夹部署有项目的主体。`backend`文件夹下的`backend`存放有项目的几个主要程序,包括根路由配置文件`url.py`，设置文件`settings.py`(在这个文件的template的`DIRS`参数中设置模板文件夹路径，`LANGUAGE_CODE`设置后端主语言，`TIME_ZONE`设置时区，`ALLOWED_HOSTS`设置是否可以内网访问)，`views.py`为核心函数存放区。</br>
&emsp;&emsp; `processSection`文件夹下存放了项目的一个应用，是项目最初版本的核心之一。依赖根路由配置文件`url.py`中的` path('processSection/',include('processSection.urls')), `</br>
&emsp;&emsp;`template`文件夹存放了项目需要用到的前端代码文件。`main.html`是首页的`html`文件，也是部署有上传接口的`html`文件。`resDisplay.html`文件是展示识别结果的`html`文件。
&emsp;&emsp;`uploadedFile`文件夹是存放上传到后端的数据（也就是图片）的文件夹
&emsp;&emsp;`db.sqlite3`为项目自带的数据库

## 3. 如何使用这一项目
__以下操作推荐在项目工作空间中进行__
1. 安装项目所需的框架，模块和包
    `pip install -r requirements.txt`
2. 命令行进入`manage.py`所在的Backend文件夹，运行命令`python manage.py runserver 0.0.0.0:8000`，本设备访问时浏览器键入`http://127.0.0.1:8000/`,同一局域网下其他设备键入`服务器IP地址:8000`即可实现访问。特别的，第一次运行这一项目时，可能会出现错误，这一错误是很可能是由模型权重尚未完成下载造成的。此时如能在命令行中看到权重文件下载进度条，请待下载完成后重新启动项目即可正常运行。若这一项目部署于虚拟空间中，则在执行`python manage.py runserver 0.0.0.0:8000`前请确保已进入虚拟空间。，
3. 关闭项目：在`backend`目录下命令行`ctrl+c`

## 4.版本说明
V 0.0.1 beta 2025年1月27日</br>
完成了开源全部流程

## 5.版权说明
&emsp;&emsp; 本项目知识产权系项目全体开发者共有。任何组织，单位及个人未经允许请勿将本项目用于商业用途。
<footer>Copyright@2025 All Rights Reserved.</footer>
