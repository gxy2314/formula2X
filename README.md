# formula2X 公式识别系统

## 项目介绍

​        随着学术论文的数字化和在线共享的增加，数学公式作为学术内容的重要组成部分，其规范化复制和引用成为了一个重要问题。传统的图片、PDF等格式公式难以直接编辑和引用，这大大增加了研究工作的难度。基于对这一点的体会，我们设计了formula2X公式识别系统，旨在提供一个从数学公式图片到可编辑文本格式的自动化转换工具。项目采用Django框架，基于深度学习模型，实现了Web端的公式识别。用户可将包含公式的图片上传至Web端，formula2X可实现图片中公式的识别，并将识别结果分别以Markdown、LaTeX等格式可复制呈现。

## 项目结构

`test.py`：测试模型的最小程序
`testforweb.py`：查看Django安装情况的测试脚本
`backend`：项目主体
`BackEnd\BackEnd`：核心配置文件
`BackEnd\BackEnd\urls.py`：根路由配置
`BackEnd\BackEnd\settings.py`：项目设置（模板路径、语言、时区、内网访问权限等）
`BackEnd\BackEnd\views.py`：核心业务逻辑函数
`BackEnd\processSection`文件夹：初始版本核心功能模块
依赖根路由配置：`path('processSection/', include('processSection.urls'))`
`BackEnd\templates`：前端代码

`BackEnd\static`文件夹：CSS等静态资源

`BackEnd\templates\main.html`：首页及文件上传接口
`BackEnd\templates\resDisplay.html`：识别结果展示页
`BackEnd\uploadedFile`文件夹：用户上传图片存储目录
db.sqlite3：项目自带数据库

________________________________________
## 如何使用

以下操作推荐在项目工作空间(.venv)中进行：

#### 基础使用

1.	安装依赖
`pip install -r requirements.txt`
2.	启动服务
`cd Backend`
`python manage.py runserver 0.0.0.0:8000`
o	本机访问：http://127.0.0.1:8000/
o	局域网访问：<服务器IP地址>:8000
3.	注意事项
o	首次运行时需等待模型权重文件自动下载（命令行显示进度条）
o	虚拟环境部署需先激活环境再启动服务
o	关闭服务：在Backend目录下按 Ctrl+C
________________________________________
## 模型训练
### 环境准备

#### 安装训练依赖
​      `pip install "pix2tex[train]"`

 #### 数据准备

生成数据集
`python -m pix2tex.dataset.dataset --equations <数学公式文本路径> --images <训练集图片文件夹路径> --out <输出文件名.pkl>`
o	预生成数据集：[Google Drive下载](https://drive.google.com/drive/folders/13CA4vAmOmD_I_dSbvLp-Lf0s6KiaNfuO)（含formulae.zip图片和math.txt标签）
o	验证集/测试集需重复此步骤

#### 配置训练

##### 修改配置文件
o	编辑 pix2tex/model/settings/config.yaml
o	关键配置项：
data: <训练集.pkl路径>      # 如 dataset_train.pkl</br>
valdata: <验证集.pkl路径>  # 如 dataset_val.pkl</br>
tokenizer: <分词器路径>    # 默认 tokenizer.json</br>
num_tokens: <词汇表大小>   # 需与分词器一致</br>

##### 启动训练

`python -m pix2tex.train --config <配置文件路径>`</br>
推荐调整参数：</br>
•	batch_size</br>
•	learning_rate</br>
•	warmup_steps</br>
•	max_epochs</br>
自定义分词器（可选）</br>
`python -m pix2tex.dataset.dataset \</br>
--equations <数学公式文本路径> \</br>
--vocab-size <词汇表大小> \  # 推荐 8000</br>
--out <输出分词器.json>       # 如 custom_tokenizer.json`</br>
完成后需同步更新配置文件中的 tokenizer 路径和 num_tokens 值。</br>

##### 注意事项

1.	定期检查数据加载逻辑</br>
2.	建议使用GPU环境（显存消耗较大）</br>
3.	参考官方Colab Notebook进行云端训练</br>
________________________________________
##### 训练结束后模型文件的保存与替换

###### 模型文件的保存

在模型训练完成后，模型文件将以 .pth 格式保存，文件命名格式如下：</br>
{name}_e{epoch}_step{step}.pth</br>
其中：</br>
{name} 为模型的名称，来自于 config.yaml 配置中的 args.name</br>
{epoch} 为当前训练的轮次（e+1）</br>
{step} 为当前训练步骤编号（i）</br>
模型默认保存在：</br>
out_path = os.path.join(args.model_path, args.name)</br>
此外，训练时的 配置文件 也会自动保存：</br>
config.yaml</br>
该文件包含所有训练参数，便于后续加载或复现训练过程。</br>

###### 如何替换预训练模型

训练完成后，您需要 手动替换 formula2X 识别系统中的模型文件：</br>
找到最新的模型文件</br>
ls <模型保存目录></br>
例如：</br>
formula2X_e10_step500.pth</br>
将训练好的模型文件复制到 Web 端目录</br>
cp <新模型路径> <Web 端模型存储路径></br>
例如：</br>
cp formula2X_e10_step500.pth backend/model.pth</br>
修改 Web 端代码以加载新模型</br>
在 settings.py 或 views.py 中修改模型加载路径：</br>
MODEL_PATH = "backend/model.pth"</br>
重启 Web 服务</br>
cd Backend</br>
python manage.py runserver 0.0.0.0:8000</br>

## 版本说明

V 0.0.1 Beta | 2025年1月27日</br>
完成开源全部流程</br>

V 1.0.0 Beta | 2025年10月31日</br>

重构前端布局逻辑 重新面世</br>

## 版权说明

本项目知识产权系全体开发者共有，未经许可不得用于商业用途。</br>
Copyright @ 2025 All Rights Reserved.</br>
