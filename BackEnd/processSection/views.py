import os
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from PIL import Image
from pix2tex.cli import LatexOCR


def process(request):
    img = Image.open('E:\\projects with vscode\\python in use\\django\\formula2X\example\\test.jpg')
    model = LatexOCR()
    return HttpResponse(model(img))
