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

## 4.如何使用本项目内置的框架训练并使用属于自己的模型
1. 下载项目目录下的pix2tex文件夹，并准备训练数据，训练数据需为已标注的数据，每一批数据分为两个部分：一部分为包含公式的图片，以文件夹存储；另一部分为公式对应的latex表达式，以一个TXT文件存储，每个公式对应的latex表达式占一行。需要注意的是，文件夹中公式对应图片排列的顺序需要和TXT中公式对应的latex表达式的排列顺序保持一致。本项目给出参考训练数据可通过Google drive[下载](https://drive.google.com/drive/folders/13CA4vAmOmD_I_dSbvLp-Lf0s6KiaNfuO)
2. 安装依赖`pip install "pix2tex[train]"`
3. 用以下命令生成数据集`python -m pix2tex.dataset.dataset --equations <数据集对应的txt的路径> --images <数据集对应的图片所在的文件夹对应的路径> --out <自定义输出名>.pkl`.特别的，对于参考数据集中的`formulae.zip`，训练集`train`，测试集`test`,验证集`val`对应的txt均为`math.txt`。对于使用自定义分词器的情况，数据集生成命令为`python -m pix2tex.dataset.dataset --equations <数学公式文本路径> --vocab-size <词汇表大小> --out <输出分词器.json>`
4. 修改配置文件，自定义训练参数。部分关键参数的定义如下
   ```
   data: <训练集.pkl路径>      # 如 dataset_train.pkl
   valdata: <验证集.pkl路径>  # 如 dataset_val.pkl
   tokenizer: <分词器路径>    # 默认 tokenizer.json
   num_tokens: <词汇表大小>   # 需与分词器一致
   ```

 5. 开始训练`python -m pix2tex.train --config <配置文件路径>`。由于模型本身的结构复杂，推荐使用cuda实现训练加速
 6. 模型的保存与使用
    在模型训练完成后，模型文件将以 .pth 格式保存，文件命名格式如下：{name}_e{epoch}_step{step}.pth。其中：
    ```
    {name} 为模型的名称，来自于 config.yaml 配置中的 args.name
    {epoch} 为当前训练的轮次（e+1）
    {step} 为当前训练步骤编号（i）
    ```
    模型默认保存在：
    `out_path = os.path.join(args.model_path, args.name)`</br>
    此外，训练时的 配置文件 也会自动保存：
    config.yaml
    完成训练后，用训练得到的模型替换项目虚拟环境中的weights.pth，再次启动项目时，系统使用的即为训练得到的模型。
   
   
## 5.版本说明
V 0.0.1 beta 2025年1月27日</br>
完成了开源全部流程</br>
v 0.1.1 beta 2025年2月12日</br>
增加了模型训练构件，增加训练说明
## 6.版权说明
&emsp;&emsp; 本项目知识产权系项目全体开发者共有。任何组织，单位及个人未经允许请勿将本项目用于商业用途。
<footer>Copyright@2025 All Rights Reserved.</footer>
