from django.http import HttpResponse
from django.shortcuts import render,redirect
import os
from PIL import Image
from pix2tex.cli import LatexOCR
from django.template import loader
import sympy as sp
from sympy.parsing.latex import parse_latex
from sympy.printing.mathml import mathml

# def test(request):
#     return HttpResponse("首发试验成功！")

# 获取项目工作空间地址
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#对应首页的视图函数，依赖模板中的main.html,url.py文件中的url(r'^',views.greating)，渲染指定的html文件
def greating(request):
    return render(request,'main.html')

#对应文件上传的视图函数，依赖url.py中的path('uploadedFile/',views.uploadFile),模板文件夹中的main.html
#项目空间中的文件夹uploadedFile(如果这个文件夹改名需要改动对应代码)
def uploadFile(request):
    if request.method=="POST":
        allowed_extensions = ['jpg', 'jpeg', 'png']
        fileGet=request.FILES.get("uploadedFile",None)#当请求方式为post时，读取文件，这个值必须和html中 <input type="file" name="uploadedFile"/>的name值一致
        #未实现文件上传，返回首页
        if not fileGet:
            # return HttpResponse("请重新上传文件",status=200)
            return redirect('/')
        #上传成功，分块写入
        if fileGet.name.split('.')[-1].lower() not in allowed_extensions:
           return redirect('/')
        storePath=open(os.path.join(BASE_DIR,'uploadedFile',fileGet.name),'wb+')
        for chunk in fileGet.chunks():
            storePath.write(chunk)
        storePath.close()
        # return HttpResponse("上传成功")
        # return render(request,'afterUpload.html')
        
        #传送到处理结果页面文件夹
        return redirect('/processed/')
    else:
        #未知的情况，返回首页
        # return HttpResponse("上传错误")
        return redirect('/')

#调用模型对上传文件进行处理，依赖模板文件夹下的resDisplay.html,工作空间中的uploadedFile文件夹，
def process(request):
    #读取最新上传到服务器中的文件
    try:
        files = [os.path.join("uploadedFile", f) for f in os.listdir("uploadedFile") if os.path.isfile(os.path.join("uploadedFile", f))]
        latest_file = max(files, key=os.path.getmtime)
        fileToProcess=latest_file
        # return HttpResponse(fileToProcess)
        # 调用模型识别
        img = Image.open(fileToProcess)
        model = LatexOCR()
        resInLatex=model(img)
        #将需要传送到前端的数据进行封装
        data={'res':model(img)}

        #加载模板
        template = loader.get_template('resDisplay.html')

        #渲染模板，其中context必须和上文中的封装一致
        # return HttpResponse(model(img))  
        return HttpResponse(template.render(context=data))
    except Exception as e:
        return redirect('/')
   